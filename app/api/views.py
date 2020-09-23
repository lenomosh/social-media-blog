from app.api import api
from flask import request, jsonify, abort
from app.db import session, db
from app.models import Pitch


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
def pitch_all():
    pitches = Pitch.query.all()
    json_pitches = []
    for pitch in pitches:
        json_pitches.append(pitch.to_dict())
    return jsonify(json_pitches)

@api.route('/pitch/<int:id>',methods=['DELETE'])
def pitch_delete(id):
    pitch = Pitch.query.get(id)
    session.delete(pitch)
    session.commit()
    return jsonify(pitch.to_dict())

@api.route('/pitch/<int:id>',methods=['GET'])
def pitch_view(id):
    pitch = Pitch.query.get(id)
    return pitch.to_dict()