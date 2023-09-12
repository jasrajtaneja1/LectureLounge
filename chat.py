from flask import render_template, request, Blueprint
from flask_login import login_required, current_user
from flask_socketio import send, join_room, leave_room, SocketIO
from . import socketio


chat = Blueprint('chat', __name__)


@chat.route('/chat')
@login_required
def chat_room():
    return render_template("chat.html", user=current_user)

@socketio.on('message')
def message(data):
    print(f"\n\n{data}\n\n")
    send({'msg': data['msg'], 'username': data['username'], 'timestamp': data['timestamp']}, room=data['room'])

@socketio.on('join')
def join(data):
    join_room(data['room'])
    send({'msg': data['username'] + " has joined the " + data['room'] + " room."}, room=data['room'])

@socketio.on('leave')
def leave(data):
    leave_room(data['room'])
    send({'msg': data['username'] + " has left the " + data['room'] + " room."}, room=data['room'])