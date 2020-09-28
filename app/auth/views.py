from app.auth import auth
from flask import request, jsonify, current_app, url_for
from app.models import User
from app.db import add, commit, or_
from flask_jwt_extended import jwt_required, get_jwt_identity, jwt_refresh_token_required, get_raw_jwt
from app import jwt
from app.mailer import send_email


blacklist = set()


@auth.route('/user/<int:user_id>')
def user_read(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(description="User not found"), 404

    return jsonify(user.to_dict())


@auth.route('/register', methods=("POST",))
def user_create():
    user_req = request.get_json()
    user = User.query.filter_by(email=user_req['email']).first()
    if user:
        # return jsonify(user.to_dict(only=("name", "email", "username",))), 200
        return jsonify(description="User with the email  already exist"), 409

    user = User.query.filter_by(username=user_req['username']).first()
    if user:
        return jsonify(description="User with the username already exist"), 409
    user = User(
        email=user_req['email'],
        username=user_req['username'],
        name=user_req['name'],
        password=user_req['password']
    )
    # user.options(joinedload_all('*'))
    user.hash_password(user_req['password'])
    add(user)
    commit()
    user_dup = user.to_dict()
    token =  user.generate_auth_token()
    send_email(
        "[ONE MINUTE PITCH] Welcome",
        'lenomosh@gmail.com',
        user_dup['email'],
        user_dup['name']
    )
    return jsonify({'token':token}), 201, {
        'Location': url_for('auth.user_read', user_id=user_dup['id'], _external=True)}


@auth.route('/login', methods=("POST",))
def user_login():
    body = request.get_json()
    username = body.get('username')

    try:
        password = body.get('password')
    except KeyError:
        password = None
    user = User.verify_auth_token(username)
    if not user:
        # This means that the auth token is wrong, now we;re trying to auth with username/password

        user = User.query.filter(
            or_(
                User.email == username,
                User.username == username

            )).first()
        if not user:
            return jsonify(description='User with the email/username provided does not exist'), 404
        if not (user.verify_password(password)):
            return jsonify(description="The password you provided was incorrect!"), 401
        access_token = user.generate_auth_token(60)
        refresh_token = user.generate_refresh_token(60)
    return jsonify(user=user.to_dict(only=("name", "email", "username","id","profile_picture.id")), access_token=access_token,
                   refresh_token=refresh_token), 200


@auth.route('/logout', methods=("GET",))
@jwt_required
def user_logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"response": "Successfully logged out"}), 200


@auth.route('/refresh_token')
@jwt_refresh_token_required
def get_refresh_token():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify(refresh_token=user.generate_refresh_token())


@jwt.token_in_blacklist_loader
def is_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist
