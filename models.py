from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(32), primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False, index=True)
    create_time = db.Column(db.Integer(20), nullable=False)
    password_hash = db.Column(db.String(128))
    update_time = db.Column(db.Integer(20), nullable=False)

    def __repr__(self):
        return '<User %s >' % self.name

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
