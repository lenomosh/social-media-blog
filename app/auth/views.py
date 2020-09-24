from app.auth import auth
from flask import request, jsonify, abort
from app.models import User
from app.db import add, commit, or_
from werkzeug.security import check_password_hash, generate_password_hash


@auth.route('/register', methods=("POST",))
def user_create():
    user_req = request.get_json()
    # return user_req
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
    return jsonify(user.to_dict())


@auth.route('/login', methods=("POST",))
def user_login():
    user_req = request.get_json()
    user = User.query.filter_by(or_(
        email=user_req['email'],
        username=user_req['email']
    ))
    if not user:
        abort(404, 'User with the email/username provided does not exist')
    if not(user_req['password'] == check_password_hash(user.password )):
        abort(401, "The password you provided was incorrect!")


