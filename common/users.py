from datetime import datetime, timezone, timedelta
from common.libs import *

class User:
    def __init__(self, id):
        self.id_ = id
        self.JST_ = timezone(timedelta(hours=+9), 'JST')
        self.start_t_ = 0
        self.watching = False
        self.detector_ = SightDetector()

    def start_watching(self):
        """Userが画面を見始めたらスタート時刻を記録"""
        if not self.watching:
            self.start_t_ = datetime.now(self.JST_)
            self.watching = True

    def end_watching(self):
        """Userが画面見ていない判定になったら開始時刻と終了時刻をDBへ記録"""
        if self.watching:
            self.record_watching_time()
            self.watching = False

    def record_watching_time(self):
        document_update(self.id_, self.start_t_, datetime.now(self.JST_))

    def img_process(self, img):
        self.detector_.detect(img)
        self.detector_.print_debug()


class Users:
    def __init__(self):
        self.n = 0
        self.login_users = {}

    def add_login_user(self, id):
        """ログインしているUserの追加"""
        if id not in self.login_users.keys():
            self.login_users[id] = User(id)
            self.n += 1
        else:
            print('This user is already login!')

    def logout_user(self, id):
        """ログアウトしたUserの削除"""
        if id in self.login_users.keys():
            del(self.login_users[id])
            self.n += 1
        else:
            print('logout error!')

    def get_user(self, id):
        """idを指定してUserの取得"""
        if id in self.login_users.keys():
            return self.login_users[id]

