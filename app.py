#pip install pillow
# pip install "pandas<0.25.0"
# pip install numpy

from flask import Flask, render_template, url_for, redirect, request, Response  #追加
from camera import VideoCamera 
from PIL import Image
import numpy as np
import cv2
import io
from common.users import Users


app = Flask(__name__, static_folder='html/static', template_folder='html/templates')
users = Users()
id = 'MYhvegA3WtTY3D67pqJANKHsxoX2'

@app.route('/')
def main():
    #return name
    return redirect(url_for('login'))

@app.route('/login.html')
def login():
    #return name
    return render_template("login.html") #変更

@app.route('/signup.html')
def signup():
    #return name
    return render_template("signup.html") #変更



@app.route('/index/<user_id>')
def index(user_id):
    # show the post with the given id, the id is an integer
    users.add_login_user(id) #追加

    return render_template('index.html',\
        user_id = user_id)


@app.route("/img", methods=["POST"])
def img():
    #画像処理部分

    # どのユーザーの画像か
    user = users.get_user(id) #追加
    img = request.files["video"].read()
    # pillow から opencvに変換
    imgPIL = Image.open(io.BytesIO(img))
    imgCV = np.asarray(imgPIL)
    # imgCV = cv2.bitwise_not(imgCV)
    # cv2.imwrite('./test.jpg', imgCV)

    # print('Get Image!!')
    user.img_process(imgCV) #追加

    return "success"

@app.route('/feed')
def feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen():
    while True:
        with open('./test.jpg', 'rb') as f:
            img = f.read()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')
## おまじない
if __name__ == "__main__":
    app.run(  threaded=True, debug=True)
    # ssl_context=('openssl/server.crt', 'openssl/server.key'),