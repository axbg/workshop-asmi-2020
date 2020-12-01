from time import sleep
from threading import Thread
from base64 import b64encode, b64decode
from requests.exceptions import ConnectionError

import os
import sys
import cv2
import requests
import numpy as np

def upload_image(url, data):
    try:
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, headers=headers, data=data)
    except ConnectionError as ex:
        print("Couldn't send the image in the cloud")
        pass   

def capture_pictures(cam, folder, url):
    while True:
        for image_file in os.listdir(folder):
            img = cv2.imread(os.path.join(folder, image_file))
      
            if img is not None:
                data = b64encode(img)
                upload_image(url, data)
                
                sleep(5)
            
def capture_frames(cam, url): 
    while True:
        _, frame = cam.read()
        image = cv2.imencode(".jpg", frame)[1]
        
        data = b64encode(image)
        upload_image(url, data)
      
        sleep(5)
        
def display_stream(cam):
    while True:
        _, frame = cam.read()
        
        cv2.imshow('Camera stream', frame)
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
def main():
    cam = cv2.VideoCapture(0)
    
    if len(sys.argv) != 2:
        print("Please give one parameter: live, disk or debug")
        exit(1)
        
    if sys.argv[1] == 'live':
        capture_pictures(cam, './samples', "http://localhost:8080")
    elif sys.argv[1] == 'disk':
        capture_frames(cam, "http://localhost:8080")
    else:
        display_stream(cam)

if __name__ == "__main__":
    main()
