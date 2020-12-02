import sys
import json 
import sqlalchemy as sa

from flask import Flask, request, jsonify
from flask_cors import CORS
from db import engine, Base, Session
from event import Event
from observer import Observer
from config import load_vars
from datetime import datetime, timedelta
from threading import Thread

def persist_event(event):
    session = Session()
    session.add(event)
    session.commit()
    session.close()

def get_last_events(days):
    session = Session()
    query_result = session.query(sa.func.concat(sa.func.day(Event.timestamp), '/', sa.func.month(Event.timestamp), '/', sa.func.year(Event.timestamp)), sa.func.count(Event.id)).filter(Event.timestamp > datetime.today() - timedelta(days = days)).group_by(sa.func.year(Event.timestamp), sa.func.month(Event.timestamp), sa.func.day(Event.timestamp)).order_by(Event.timestamp).all()
    return json.dumps(query_result)

def get_events_by_day(day, month, year):
    session = Session()
    return json.dumps(session.query(sa.func.hour(Event.timestamp), sa.func.count(Event.id)).filter(sa.extract('day', Event.timestamp) == day, sa.extract('month', Event.timestamp) == month, sa.extract('year', Event.timestamp) == year).group_by(sa.func.hour(Event.timestamp)).order_by(Event.timestamp).all())

env_vars = load_vars()

Base.metadata.create_all(engine)
observer = Observer(4, env_vars['AWS_ACCESS_KEY'], env_vars['AWS_SECRET_KEY'])
app = Flask("collector")

CORS(app)


@app.route("/", methods=['GET'])
def index():
    return "collector is running" 

@app.route("/data", methods=['GET'])
def get_data():
    try:
        days = int(request.args.get('days'))
        if days is None or days > 365:
            raise ValueError
    except (ValueError, TypeError):
        days = 10

    return get_last_events(days)

@app.route('/detail', methods=['GET'])
def get_detailed_day():
    try:
        day = int(request.args.get('day'))
        month = int(request.args.get('month'))
        year = int(request.args.get('year'))

        if day is None or day > 31 or month is None or month > 12 or year is None or year < 2018 or year > 2022: 
            raise ValueError
    except (ValueError, TypeError) as ex:
        return "Bad request", 400

    return get_events_by_day(day, month, year)

@app.route("/collect", methods = ['POST'])
def collect():
    payload = request.get_json()

    try:
        if "image" not in payload.keys():
            return jsonify(message="Invalid request"), 400

        found_event = observer.analyze_picture(payload["image"])

        if found_event:
            Thread(target=persist_event, args=[found_event]).start()
            print("Stored cat event")
        
        return "OK"
    except:
        raise sys.exc_info()
        return jsonify(message="An error occurred"), 500
