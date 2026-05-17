from flask import Blueprint

auth = Blueprint('auth', __name__)
@auth.route('/login')
def login():
    return 'this is the login page'

@auth.route('/signup')
def login():
    return 'this is the sign up page'