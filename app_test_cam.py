import face_recognition
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
from app import encodings, names, student
import io,os,sys

video_capture = cv2.VideoCapture(0)

# known_face_encodings = encodings
# known_face_names = names
face_locations = []
face_encodings = []
face_names = []
students = student
process_this_frame = True

while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)

    try:
        face_reg_encoding = face_recognition.face_encodings(rgb_small_frame, face_locations)
        if len(face_reg_encoding) != 0:
            face_reg_encoding = face_reg_encoding[0]
        matches = face_recognition.compare_faces(encodings, face_reg_encoding)
        name = "Unknown"
        face_names = []
        face_distances = face_recognition.face_distance(encodings, face_reg_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index] and face_distances[best_match_index]< 0.4:
            name = names[best_match_index]
        if name != "Unknown":
            students[str(name)]["check"] = "1"
            face_recognition.setlistsv(students)
        face_names.append(name)
    except Exception as e: 
        print(e)
        
    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 50), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cl = name
        if cl != "Unknown":
          cl = students[str(name)]["name"]
        cv2.putText(frame,'Ho ten: ' + cl, (left + 6, bottom - 30), font, 0.5, (255, 255, 255), 1)
        cv2.putText(frame,'Vi tri: ' + name, (left + 6, bottom), font, 0.5, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
