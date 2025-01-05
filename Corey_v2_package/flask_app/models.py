from datetime import datetime
from itsdangerous import URLSafeTimedSerializer as Serializer
from Corey_v2_package.flask_app import db_, login_manager, app_
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
db_.metadata.clear()


class User(db_.Model, UserMixin):
    id = db_.Column(db_.Integer, primary_key=True)
    username = db_.Column(db_.String(20), unique=True, nullable=False)
    email = db_.Column(db_.String(120), unique=True, nullable=False)
    image_file = db_.Column(db_.String(20), nullable=False, default='default.jpg')
    password = db_.Column(db_.String(60), nullable=False)
    posts = db_.relationship('Post', backref='author',lazy=True)

    def get_reset_token(self):
        s = Serializer(app_.config['SECRET_KEY'])
        return s.dumps({'user_id':self.id})

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app_.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}','{self.image_file}')"

class Post(db_.Model):
    id = db_.Column(db_.Integer, primary_key=True)
    title = db_.Column(db_.String(100), nullable=False)
    date_posted = db_.Column(db_.DateTime, nullable=False, default=datetime.utcnow)
    content = db_.Column(db_.Text, nullable=False)
    user_id = db_.Column(db_.Integer, db_.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"
