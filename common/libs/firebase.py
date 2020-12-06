import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import config.setting as setting

FIREBASE_KEY = setting.FIREBASE_KEY

# Use a service account
cred = credentials.Certificate(FIREBASE_KEY)
firebase_admin.initialize_app(cred)
db = firestore.client()

def document_set(id):
    """usersのid指定でtimeデータを初期化"""
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
        if 'time' not in doc:
            """timeフィールドがなかったら作る"""
            doc_ref.update({
                u'time': {
                    u'start': [start_t],
                    u'end'  : [end_t],
                }
            })
        else:
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

def update_slack_info(id, token, channels):
    doc_ref = db.collection(u'users').document(id)
    doc_ref.update({
        u'slack_token'  : token,
        u'channels'     : channels,
    })

def get_slack_apitoken(id):
    doc_ref = db.collection(u'users').document(id)
    try:
        doc = doc_ref.get().to_dict()
        if 'slack_token' in doc:
            """slack_apiの情報があったら"""
            return doc['slack_token']
        else:
            return False
    except google.cloud.exceptions.NotFound:
        print('No such document!')

def get_slack_channels(id):
    doc_ref = db.collection(u'users').document(id)
    try:
        doc = doc_ref.get().to_dict()
        if 'channels' in doc:
            """channelsの情報があったら"""
            return doc['channels']
        else:
            return False
    except google.cloud.exceptions.NotFound:
        print('No such document!')

def document_print(id):
    """documentのidの人の内容を出力"""
    doc_ref = db.collection(u'users').document(id)
    doc = doc_ref.get().to_dict()
    print(doc)
    return
