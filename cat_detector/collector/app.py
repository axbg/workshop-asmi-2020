import sys
import json 

from flask import Flask, request, jsonify
from db import engine, Base, Session
from event import Event
from observer import Observer
from config import load_vars
from threading import Thread


def persist_event(event):
    session = Session()
    session.add(event)
    session.commit()
    session.close()

def get_events():
    session = Session()
    return session.query(Event).all()


env_vars = load_vars()

Base.metadata.create_all(engine)
observer = Observer(2, env_vars['AWS_ACCESS_KEY'], env_vars['AWS_SECRET_KEY'])
app = Flask("collector")


@app.route("/", methods = ['GET'])
def index():
    return "collector is running" 

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
