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
    """usersコレクションへデータ追加"""
    doc_ref = db.collection(u'users').document(id)
    try:
        doc = doc_ref.get().to_dict()
        doc_ref.update({
            # u'id'           : doc['id'],
            # u'login_count'  : doc['login_count'],
            # u'mail'         : doc['mail'],
            # u'name'         : doc['name'],
            # u'state'        : doc['state'],
            u'time': {
                u'start': [],
                u'end'  : [],
            }
        })
    except google.cloud.exceptions.NotFound:
        print('No such document!')
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
