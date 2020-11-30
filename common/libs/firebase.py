import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import config.setting as setting

FIREBASE_KEY = setting.FIREBASE_KEY

# Use a service account
cred = credentials.Certificate(FIREBASE_KEY)
firebase_admin.initialize_app(cred)
db = firestore.client()

def document_set(id, name):
    """usersコレクションへデータ追加・上書き"""
    doc_ref = db.collection(u'users').document(id)
    doc_ref.set({
        u'id'  : id,
        u'mail': u'hogehoge@hoge.com',
        u'name': name,
        u'time': {
            u'start': [],
            u'end'  : [],
        }
    })
    return

def document_update(id, start_t, end_t):
    """usersのid指定でのデータを更新(time)"""
    doc_ref = db.collection(u'users').document(id)
    try:
        doc = doc_ref.get().to_dict()
        start = doc['time']['start']
        end = doc['time']['end']
        start.append(start_t)
        end.append(end_t)
        doc_ref.update({
            u'time': {
                u'start': start,
                u'end'  : end,
            }
        })
    except google.cloud.exceptions.NotFound:
        print('No such document!')
    return

def document_print(id):
    """documentのidの人の内容を出力"""
    doc_ref = db.collection(u'users').document(id)
    doc = doc_ref.get().to_dict()
    print(doc)
    return
