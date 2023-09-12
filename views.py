from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def HomeLanding():
    return render_template("home.html", user = current_user)

@views.route('/learnmore')
def LearnMore():
    return render_template("learnmore.html", user = current_user)

@views.route('/chatrooms')
@login_required
def ChatRooms():
    return render_template("ChatRooms.html", user = current_user)





