import face_recognition
import cv2
import numpy as np
from PIL import Image
import io,os,sys
encodings = []
names =[]

def getData(encodings, names):
    dir = "image1/"
    train_dir = os.listdir(dir)
    for person in train_dir: 
        pix = os.listdir(dir + person) 
        for i in range(3):
            print("đang trainning ảnh " + str(i) + "của " + person)
            face = face_recognition.load_image_file( 
                dir + person + "/" + pix[i]) 
            face_bounding_boxes = face_recognition.face_locations(face,number_of_times_to_upsample=0, model="cnn") 
            if len(face_bounding_boxes) == 1: 
                face_enc = face_recognition.face_encodings(face,face_bounding_boxes)[0] 
                encodings.append(face_enc) 
                names.append(person)
            else: 
                print(person + "/" + pix[i] + " khong the sd de training")
            print("Training thành công")
    return encodings, names
    
def checkAcc(encodings, names):
    numAC = 0
    total = 0
    dir = "image1/"
    train_dir = os.listdir(dir)
    for person in train_dir: 
        pix = os.listdir(dir + person) 
        for i in range(4, 9):
            print("đang xác định ảnh " + str(i) + "của " + person)
            face = face_recognition.load_image_file( 
                dir + person + "/" + pix[i]) 
            face_bounding_boxes = face_recognition.face_locations(face,number_of_times_to_upsample=0, model="cnn") 
            if len(face_bounding_boxes) == 1: 
                face_reg_encoding = face_recognition.face_encodings(face, face_bounding_boxes)
                if len(face_reg_encoding) == 0:
                    return {"msg" : "không tìm thấy người nào trong ảnh"}
                else:
                  face_reg_encoding = face_reg_encoding[0]
                  matches = face_recognition.compare_faces(encodings, face_reg_encoding)
                  name = "Unknown"
                  face_distances = face_recognition.face_distance(encodings, face_reg_encoding)
                  best_match_index = np.argmin(face_distances)
                  if matches[best_match_index] and face_distances[best_match_index]< 0.4:
                      name = names[best_match_index]
                      if name == person:
                        numAC = numAC + 1
                        print("Nhận diện đúng")
                      else:
                        print("nhận diện không đúng")
    print("AC" + str(numAC))

[encodings, names] = getData(encodings, names)
checkAcc(encodings, names)
