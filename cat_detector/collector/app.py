import sys
import sqlalchemy as sa
import json 

from flask import Flask, request, jsonify
from db import engine, Base, Session
from event import Event
from observer import Observer
from config import load_vars
from datetime import datetime, timedelta
from threading import Thread

def serialize(query_result):
    return list(map(lambda x: x.to_json(), query_result))

def persist_event(event):
    session = Session()
    session.add(event)
    session.commit()
    session.close()

def get_last_events(days):
    session = Session()
    query_result = session.query(sa.func.concat(sa.func.year(Event.timestamp), '/', sa.func.month(Event.timestamp), '/', sa.func.day(Event.timestamp)), sa.func.count(Event.id)).filter(Event.timestamp > datetime.today() - timedelta(days = days)).group_by(sa.func.year(Event.timestamp), sa.func.month(Event.timestamp), sa.func.day(Event.timestamp)).order_by(Event.timestamp).all()
    return json.dumps(query_result)

def get_all_events():
    session = Session()
    return json.dumps(serialize(session.query(Event).all()))


env_vars = load_vars()

Base.metadata.create_all(engine)
observer = Observer(4, env_vars['AWS_ACCESS_KEY'], env_vars['AWS_SECRET_KEY'])
app = Flask("collector")


@app.route("/", methods = ['GET'])
def index():
    return "collector is running" 

@app.route("/data", methods=['GET'])
def data():
    try:
        days = int(request.args.get('days'))
        if days is None or type(days) != int or days > 365:
            raise ValueError
    except (ValueError, TypeError):
        days = 10

    return get_last_events(days)

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
