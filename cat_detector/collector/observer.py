import boto3

from datetime import datetime, timedelta
from base64 import b64decode
from event import Event


class Observer:
    def __init__(self, missed_frame_counter, bucket, access_id, access_key):
        self.found = False
        self.found_timestamp = None
        self.lost_timestamp = None
        self.last_time_saved = None
        self.frame_counter_default = self.missed_frame = missed_frame_counter
        self.cat_picture = None
        self.bucket_name = bucket
        self.bucket_client = boto3.client(
            's3', region_name='eu-central-1', aws_access_key_id=access_id, aws_secret_access_key=access_key)
        self.rekog_client = boto3.client(
            'rekognition', region_name='eu-central-1', aws_access_key_id=access_id, aws_secret_access_key=access_key)

    def get_last_pictures(self, n):
        bucket_location = self.bucket_client.get_bucket_location(
            Bucket=self.bucket_name)['LocationConstraint']
            
        pictures = self.bucket_client.list_objects_v2(
            Bucket=self.bucket_name)['Contents']

        no_of_pictures = len(pictures)

        if no_of_pictures < n:
            n = no_of_pictures

        result = list(map(lambda x: "https://{}.s3.{}.amazonaws.com/{}".format(
            self.bucket_name, bucket_location, x["Key"]), pictures[-n:]))[::-1]

        return result

    def analyze_picture(self, image):
        decoded_image = b64decode(image)

        response = self.rekog_client.detect_labels(
            Image={'Bytes': decoded_image})

        labels = list(map(lambda a: a['Name'], response['Labels']))

        if "Cat" in labels:
            self.found = True
            self.missed_frame = self.frame_counter_default
            self.lost_timestamp = None

            if self.found_timestamp is None:
                self.cat_picture = decoded_image
                self.found_timestamp = datetime.now()
                print("Cat found at: {}". format(self.found_timestamp))
        elif self.found:
            if self.missed_frame > 0:
                self.missed_frame -= 1

                if self.lost_timestamp is None:
                    self.lost_timestamp = datetime.now()
            else:
                self.bucket_client.put_object(Bucket=self.bucket_name, Key="{}.jpg".format(
                    self.found_timestamp.strftime("%Y_%m_%d_%H:%M:%S")), Body=self.cat_picture, ACL="public-read")
                return self.create_event()
        return False

    def create_event(self):
        estimated_duration = (self.lost_timestamp -
                              self.found_timestamp).total_seconds() / 60

        duration = estimated_duration if estimated_duration != 0 else 1
        ev = Event(timestamp=self.found_timestamp, duration=duration)

        self.found = False
        self.found_timestamp = None

        return ev
