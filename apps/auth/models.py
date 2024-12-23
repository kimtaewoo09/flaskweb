from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash

class User_auth(db.Model):
    __tablename__="users_auth"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String, index=True)
    email=db.Column(db.String, index=True)
    #userid=db.Column(db.String, index=True)
    password_hash=db.Column(db.String)
    create_at=db.Column(db.DateTime, default=datetime.now)
    updatw_at=db.Column(db.DateTime, default=datetime.now,onupdate=datetime.now)

    @property
    def password(self):
        raise AttributeError('읽어 들일 수 없습니다')
    @password.setter
    def password(self, password):
        self.password_hash=generate_password_hash(password)
    