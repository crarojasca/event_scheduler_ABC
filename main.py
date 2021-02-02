from . import db

from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user


main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.home')) 
    return redirect(url_for('auth.login')) 

@main.route('/home')
@login_required
def home():
    return render_template('home.html', name=current_user.name)

@main.route('/event', methods=['POST'])
def create_event():
    category = request.form.get('category')
    place = request.form.get('place')
    adress = request.form.get('adress')
    date_start = request.form.get('date_start')
    date_end = request.form.get('date_end')

    print('DATOS:', category, place, adress, date_start, date_end)

    return redirect(url_for('main.home')) 