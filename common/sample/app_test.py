from flask import Flask, render_template, request
import numpy as np
import cv2

from image_process import canny

app = Flask(__name__) 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello") 
def hello():
    return "Hello Flask!"

@app.route("/upload", methods=["POST"])  #追加
def upload():
    stream = request.files['file'].stream
    img_array = np.asanyarray(bytearray(stream.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, 1)
    height, width, channels = img.shape[:3]
    print("width: " + str(width))
    print("height: " + str(height))
    canny(img)
    print("get image!")
    return "ようこそ、" + request.form["username"] + "さん"

if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run(debug=False)