from flask import Flask,request,jsonify
import face_recognition
import cv2
import numpy as np
from PIL import Image
import io,os,sys
encodings = []
names =[]
app = Flask(__name__)
student = face_recognition.getlistsv_train()
@app.route('/check', methods=['POST'])
def check():
    global encodings
    global names
    name = []
    cl = []
    image = request.files['image']
    img = Image.open(image)
    img = np.array(img)
    try:
        face_reg_encoding = face_recognition.face_encodings(img)
        if len(face_reg_encoding) == 0:
            return {"msg" : "Khong tim thay nguoi trong anh"}
        else:
            face_reg_encoding = face_reg_encoding[0]
        matches = face_recognition.compare_faces(encodings, face_reg_encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(encodings, face_reg_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index] and face_distances[best_match_index]< 0.4:
            name = names[best_match_index]
        if name != "Unknown":
            student[str(name)]["check"] = "1"
            face_recognition.setlistsv(student)
    except Exception as e: 
        print(e)
        name = "Unknown"
    cl = name
    if cl != "Unknown":
      cl = student[str(name)]["name"]
    else:
      cl="Unknown"
    return {
      "name": cl,
      "vt": str(name)
    }
def getData(encodings, names):
    dir = "image/"
    train_dir = os.listdir(dir)
    for person in train_dir: 
        pix = os.listdir(dir + person) 
        for person_img in pix: 
            face = face_recognition.load_image_file( 
                dir + person + "/" + person_img) 
            # face_bounding_boxes = face_recognition.face_locations(face,number_of_times_to_upsample=0, model="cnn") 
            face_bounding_boxes = face_recognition.face_locations(face) 
            if len(face_bounding_boxes) == 1: 
                face_enc = face_recognition.face_encodings(face,face_bounding_boxes)[0] 
                encodings.append(face_enc) 
                names.append(person)
            else: 
                print(person + "/" + person_img + " khong the sd de training") 
    return  encodings,names
[encodings, names] = getData(encodings, names)
@app.route('/getallsv', methods=['POST'])
def getallsv():
    return jsonify(face_recognition.getlistsv())
if __name__ == '__main__':
    app.run(host= '0.0.0.0')