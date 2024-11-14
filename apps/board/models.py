from datetime import datetime
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Boards(db.Model, UserMixin):
    __tablename__ = 'boards'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # 게시글 제목
    content = db.Column(db.Text, nullable=False)       # 게시글 내용
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # 글쓴이 ID
    views = db.Column(db.Integer, default=0)  # 조회수
    created_at = db.Column(db.DateTime, default=datetime.now)  # 생성 시각
    updated_at = db.Column(db.DateTime, onupdate=datetime.now) # 수정 시각

    author = db.relationship('User', backref=db.backref('posts', lazy=True))
    
