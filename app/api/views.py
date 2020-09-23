from app.api import api
from flask import request, jsonify
from app.db import session
from app.models import Pitch, Comment


# Pitch CRUD ###########################################
@api.route('/pitch', methods=['POST'])
def pitch_create():
    user_id = request.form.get('user_id')
    category_id = request.form.get('category_id')
    content = request.form.get('content')
    pitch = Pitch(user_id=user_id, category_id=category_id, content=content)
    # try:
    session.add(pitch)
    session.commit()
    pitch = Pitch.query.get(pitch.id).to_dict()

    return jsonify(pitch)
    # except:
    #     abort(503)


@api.route('/pitch', methods=['GET'])
def pitch_index():
    pitches = Pitch.query.all()
    json_pitches = []
    for pitch in pitches:
        json_pitches.append(pitch.to_dict())
    return jsonify(json_pitches)


@api.route('/pitch/<int:id>', methods=['DELETE'])
def pitch_delete(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    session.delete(pitch)
    session.commit()
    return jsonify(pitch.to_dict())


@api.route('/pitch/<int:id>', methods=['GET'])
def pitch_read(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    return pitch.to_dict()


# Pitch CRUD ###########################################

# Comment CRUD ###########################################


@api.route('/comment', methods=['POST'])
def comment_create():
    req_data = request.get_json()
    comment = Comment(**req_data)
    session.add(comment)
    session.commit()
    return comment.to_dict()


@api.route('/comment', methods=['GET'])
def comment_index():
    comments = Comment.query.all()
    comment_json = []
    for comment in comments:
        comment_json.append(comment.to_dict())

    return jsonify(comment_json)


@api.route('/comment/<int:comment_id>', methods=("GET",))
def comment_read(comment_id):
    comment = Comment.query.get(comment_id)
    return jsonify(comment.to_dict())


@api.route('/comment/<int:comment_id>',methods=("DELETE",))
def comment_delete(comment_id):
    comment = Comment.query.get(comment_id)
    session.delete(comment)
    session.commit()
    return jsonify(comment.to_dict())