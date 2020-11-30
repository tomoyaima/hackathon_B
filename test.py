"""
テスト用
"""
from common.users import Users
import time

# app.pyではusersを宣言
users = Users()
# ログインが確認されたらusersのdicにuserを追加
users.add_login_user('alovelace')
# userの情報がほしいならget_userする
user = users.get_user('alovelace')
# 勉強開始時間を記録
user.start_watching()
# 五秒待つ
time.sleep(5)
# 勉強が終わったらfirebaseに開始時刻と終了時刻を記録
user.end_watching()

