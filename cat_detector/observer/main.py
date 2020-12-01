from time import sleep

import cv2
import requests

def capture_picture():
    pass

def capture_frames():
    cam = cv2.VideoCapture(0)

    while True:
        _, frame = cam.read()
        image = cv2.imencode(".jpg", frame)[1]

        data = image.tostring()
        headers = {'Content-Type': 'application/json'}

        # r = requests.post("http://localhost:8080", headers=headers, data=data)

        cv2.imshow(image)

        sleep(10)

def main():
    capture_frames()

if __name__ == "__main__":
    main()