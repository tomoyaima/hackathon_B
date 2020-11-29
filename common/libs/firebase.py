import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import common.libs.setting as setting

FIREBASE_KEY = setting.FIREBASE_KEY
# Use a service account
cred = credentials.Certificate(FIREBASE_KEY)
firebase_admin.initialize_app(cred)

db = firestore.client()

def document_set(id, name):
    """usersコレクションのデータ追加・上書き"""
    doc_ref = db.collection(u'users').document(id)
    doc_ref.set({
        u'id'  : id,
        u'mail': u'hogehoge@hoge.com',
        u'name': name,
    })
    return

def document_update(id, name):
    """usersコレクションのデータを更新"""
    doc_ref = db.collection(u'users').document(id)
    doc_ref.update({
        u'id'  : id,
        u'name': name,
    })
    return

def collection_get():
    """usersコレクション内の内容を出力"""
    docs = db.collection(u'users').get()
    for doc in docs:
        print(doc.id, doc.to_dict())
    return
