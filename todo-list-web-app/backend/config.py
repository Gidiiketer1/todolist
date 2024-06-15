# backend/config.py

class Config:
    SECRET_KEY = b'\x9c\x0bJ\xa7\xe9\xd8\xa1\x18\xe8\xddA\xf6\xa8\x9e\xd2\xf8\x90\xdc\xbd\xd5\xb6\x7f\x07'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/todo_list_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
