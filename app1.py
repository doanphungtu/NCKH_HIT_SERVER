from flask import Flask,request
import cv2
import face_recognition
import numpy as np
from PIL import Image
import io,os,sys
app = Flask(__name__)
@app.route('/getallsv', methods=['POST'])
def getallsv():
    return face_recognition.getlistsv()
if __name__ == '__main__':
    app.run(host= '0.0.0.0')