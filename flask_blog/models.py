from datetime import datetime

from flask_blog import db, login_manager
from flask_login import UserMixin
from flask_blog import constants


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    

class User(db.Model, UserMixin):
    """
    Модель пользователя
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.SmallInteger, default=constants.USER)
    status = db.Column(db.SmallInteger, default=constants.NEW)
    posts = db.relationship('Post', backref='author', lazy=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')

    def getStatus(self):
        return constants.STATUS[self.status]

    def getRole(self):
        return constants.ROLE[self.role]

    def __repr__(self) -> str:
        return f'Пользователь {self.username}, {self.email}, {self.image_file}'


class Post(db.Model):
    """
    модель поста
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f'Запись({self.title}, {self.date_posted})'
