from app.auth import auth
from flask import request, jsonify, abort
from app.models import User
from app.db import add, commit, or_
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, current_user, logout_user, login_required
# from app import lm as login_manager
from app import lm as login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth.route('/register', methods=("POST",))
def user_create():
    user_req = request.get_json()
    user = User.query.filter_by(email=user_req['email']).first()
    if user:
        return abort(409, "User with the email or username already exist")
    user = User(
        email=user_req['email'],
        username=user_req['password'],
        name=user_req['name'],
        password=generate_password_hash(
            user_req['password'],
            method='sha256'
        ))
    add(user)
    commit()
    login_user(user)

    return jsonify(user.to_dict())


@auth.route('/login', methods=("POST",))
def user_login():
    user_req = request.get_json()
    user = User.query.filter(
        or_(
            User.email == user_req['email'],
            User.username == user_req['email']

        )).first()
    if not user:
        abort(404, 'User with the email/username provided does not exist')
    if not (check_password_hash(user.password, user_req['password'])):
        abort(401, "The password you provided was incorrect!")
    login_user(user, remember=True if user_req['remember'] else False)
    return jsonify(current_user.to_dict())


@auth.route('/logout', methods=("GET",))
@login_required
def user_logout():
    logout_user()
    return jsonify("Success")
