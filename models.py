from . import db
from flask_login import UserMixin
from datetime import datetime


    
# Define the User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile_picture = db.Column(db.String(20), nullable=False, default='default.jpg')
    bio = db.Column(db.Text, nullable=True)
    courses = db.relationship('Course', secondary='user_courses')
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))

# Define the Course model
class Course(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(10), nullable=False, unique=True)
    chat_rooms = db.relationship('ChatRoom', backref='course', lazy=True)

# Define User-Course association table
user_courses = db.Table('user_courses',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
)

# Define the ChatRoom model
class ChatRoom(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    messages = db.relationship('Message', backref='chat_room', lazy=True)

# Define the Message model
class Message(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    chat_room_id = db.Column(db.Integer, db.ForeignKey('chat_room.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Create tables

    