import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print('BASE_DIR 경로:' + str(BASE_DIR))

secret_file = os.path.join(BASE_DIR, 'secrets.json')
with open(secret_file) as f:
    secrets = json.loads(f.read())
# print('secrets 데이터:' + str(secrets))


def get_secret():
    return secrets['SECRET_KEY']