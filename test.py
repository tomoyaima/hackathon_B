"""
テスト用
"""
from common.users import Users
import time
import cv2

# app.pyではusersを宣言
users = Users()
# ログインが確認されたらusersのdicにuserを追加
users.add_login_user('HAqbTQvzyUbMBY83xDWy2rj3pwt1')
# userの情報がほしいならget_userする
user = users.get_user('HAqbTQvzyUbMBY83xDWy2rj3pwt1')
# img = cv2.imread('test.jpg')
# print("Get image!!")
# user.img_process(img)

# user.slack_message()
user.get_image_path()

# # 勉強開始時間を記録
# user.start_watching()
# # 五秒待つ
# time.sleep(5)
# # 勉強が終わったらfirebaseに開始時刻と終了時刻を記録
# user.end_watching()

