from flask import Flask, request, jsonify
from db import engine, Base, Session
from event import Event
from datetime import datetime, timedelta

import json 

def persist_event(event):
    session = Session()
    session.add(event)
    session.commit()
    session.close()

def get_events():
    session = Session()
    return session.query(Event).all()


Base.metadata.create_all(engine)
app = Flask("collector")

@app.route("/", methods = ['GET'])
def index():
    return "collector is running" 


@app.route("/collect", methods = ['POST'])
def collect():
    payload = request.get_json()
    try:
        if "data" not in payload.keys():
            return jsonify(message="Invalid request"), 400

        # handle data

        return "OK"
    except:
        return jsonify(message="An error occurred"), 500