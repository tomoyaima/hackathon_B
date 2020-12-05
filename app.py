#pip install pillow
# pip install "pandas<0.25.0"
# pip install numpy

from flask import Flask, render_template, url_for, redirect, request, Response, jsonify #追加
from camera import VideoCamera 
from PIL import Image
import numpy as np
import cv2
import io
from common.users import Users


app = Flask(__name__, static_folder='html/static', template_folder='html/templates')
users = Users()

@app.route('/')
def main():
    #return name
    return redirect(url_for('login'))

@app.route('/stop/<user_id>')
def stop(user_id):
    #return name
    user = users.get_user(user_id)
    user.end_watching()
    return redirect(url_for("index",\
        user_id = user_id))

@app.route('/rank/<user_id>')
def rank(user_id):
    #return name
    return render_template("rank.html")


@app.route('/time/<user_id>')
def time(user_id):
    #return name
       return render_template("time.html")

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
    users.add_login_user(user_id) #追加

    return render_template('index.html',\
        user_id = user_id)


@app.route('/img/<user_id>', methods=["POST"])
def img(user_id):
    """画像処理部分"""

    # どのユーザーの画像か
    user = users.get_user(user_id) #追加
    img = request.files["video"].read()

    # pillow から opencvに変換
    imgPIL = Image.open(io.BytesIO(img))
    imgCV = np.asarray(imgPIL)
    # imgCV = cv2.bitwise_not(imgCV)
    # cv2.imwrite('./test.jpg', imgCV)

    user.img_process(imgCV) # 画像処理部へ投げる

    if user.watching :
        result = 'true'
    else :
        result = 'false'
        if user.is_require_caution():
            """注意が必要ならjsonに警告レベルをくっつける"""
            return jsonify({'watching' : result, 'caution' : user.caution_level})
    return jsonify({'watching' : result})


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