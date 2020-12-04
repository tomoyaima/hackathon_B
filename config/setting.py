import os
from os.path import join, dirname
from dotenv import load_dotenv

# load_dotenv(verbose=True)
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

load_dotenv()

FIREBASE_KEY = os.environ.get('FIREBASE_KEY')
FACE_CASCADE_PATH = os.environ.get('FACE_CASCADE_PATH')
EYE_CASCADE_PATH = os.environ.get('EYE_CASCADE_PATH')
