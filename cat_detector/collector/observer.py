import boto3

from datetime import datetime, timedelta
from base64 import b64decode
from event import Event

class Observer:
    def __init__(self, missed_frame_counter, access_id, access_key):
        self.found = False
        self.found_timestamp = None
        self.lost_timestamp = None
        self.last_time_saved = None
        self.frame_counter_default = self.missed_frame = missed_frame_counter
        self.rekog = boto3.client('rekognition', region_name='eu-central-1', aws_access_key_id=access_id, aws_secret_access_key= access_key)

    def analyze_picture(self, image):
        response = self.rekog.detect_labels(Image={'Bytes': b64decode(image)})
        labels = list(map(lambda a: a['Name'] , response['Labels']))
       
        if "Cat" in labels:
            self.found = True
            self.missed_frame = self.frame_counter_default
            self.lost_timestamp = None

            if self.found_timestamp is None:
                self.found_timestamp = datetime.now()

            now = datetime.now()
            if self.last_time_saved is None or now > self.last_time_saved:
                self.last_time_saved = now + timedelta(minutes = 5)
                print("Cat found at: {}". format(now))
        elif self.found:
            if self.missed_frame > 0:
                self.missed_frame -= 1

                if self.lost_timestamp is None:
                    self.lost_timestamp = datetime.now()
            else:
                return self.create_event()
        return False

    def create_event(self):
        estimated_duration = (self.lost_timestamp - self.found_timestamp).total_seconds() / 60
        
        duration = estimated_duration if estimated_duration != 0 else 1
        
        ev = Event(timestamp=self.found_timestamp, duration=duration)

        self.found = False
        self.found_timestamp = None

        return ev
