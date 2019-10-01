import cv2 as cv
import os

if 'CAMERA_ID' in os.environ:
    camera_id = int(os.environ['CAMERA_ID'])
else:
    camera_id = 1

classifier_xml = './src/opencv-detector/model/haarcascade_frontalface_default.xml'
classifier = cv.CascadeClassifier()

if not classifier.load(classifier_xml):
    raise ValueError(f'Could not load {classifier_xml}')

video_capture = cv.VideoCapture(camera_id)

while(True):
    # Capture frame-by-frame
    video_capture_result, frame = video_capture.read()

    if video_capture_result == False:
        raise ValueError(f'Error reading the frame from camera {camera_id}')

    # face detection and other logic goes here
    faces = classifier.detectMultiScale(frame, 1.3, 5)

    for (x, y, w, h) in faces:
        # send each face in mqtt topic
        cv.rectangle(frame, (x, y), (x+w, y+h), color=(0, 255, 0), thickness=2)

    cv.imshow('Input', frame)
    if cv.waitKey(1) == 27:
        break