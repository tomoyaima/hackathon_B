"""
テスト用
"""

from common.libs.firebase import document_set, document_update, collection_get

document_set('alovelace', 'suzukidesu')
collection_get()
document_update('alovelace', 'suzukisuzusuzu')
collection_get()
