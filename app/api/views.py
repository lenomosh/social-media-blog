from app import photos
from app.api import api
from flask import request, jsonify, abort, send_from_directory, current_app
from app.db import session, add, commit, delete
from app.models import Pitch, Comment, Action, Category, User, ProfilePicture


# Pitch CRUD ###########################################
@api.route('/pitch', methods=['POST'])
def pitch_create():
    data = request.get_json()
    user_id = data['user_id']
    category_id = data['category_id']
    content = data['content']
    pitch = Pitch(user_id=user_id, category_id=category_id, content=content)
    # import pdb;pdb.set_trace()
    add(pitch)
    commit()
    pitch = Pitch.query.get(pitch.id).to_dict()
    return jsonify(pitch)


@api.route('/pitch', methods=['GET'])
def pitch_index():
    pitches = Pitch.query.all()
    # import pdb;pdb.set_trace()
    json_pitches = []
    for pitch in pitches:
        likes = Action.query.filter_by(action_type=1, pitch_id=pitch.id).count()
        dislikes = Action.query.filter_by(action_type=0, pitch_id=pitch.id).count()
        pitch = dict(**pitch.to_dict(), likes=likes, dislikes=dislikes)
        json_pitches.append(pitch)
    return jsonify(json_pitches)


@api.route('/pitch/<int:id>', methods=['DELETE'])
def pitch_delete(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    delete(pitch)
    commit()
    return jsonify(pitch.to_dict())


@api.route('/pitch/<int:pitch_id>', methods=['GET'])
def pitch_read(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    likes = Action.query.filter_by(action_type=1, pitch_id=pitch_id).count()
    dislikes = Action.query.filter_by(action_type=0, pitch_id=pitch_id).count()

    return jsonify(**pitch.to_dict(), likes=likes, dislikes=dislikes)


# Pitch CRUD ###########################################

# Comment CRUD ###########################################


@api.route('/comment', methods=['POST'])
def comment_create():
    req_data = request.get_json()
    comment = Comment(**req_data)
    add(comment)
    commit()
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


@api.route('/comment/<int:comment_id>', methods=("DELETE",))
def comment_delete(comment_id):
    comment = Comment.query.get(comment_id)
    delete(comment)
    commit()
    return jsonify(comment.to_dict())


# Comment CRUD ###########################################

# Action CRUD ###########################################
@api.route('/action', methods=("POST",))
def action_create():
    # action type
    # 1 - like
    # 0 - dislike
    req_action = request.get_json()
    catch_dups = Action.query.filter_by(user_id=req_action['user_id'], pitch_id=req_action['pitch_id']).all()
    # return jsonify([catch_dup.to_dict()['action_type'] == req_action['action_type']])
    if catch_dups:
        for catch_dup in catch_dups:
            if catch_dup.to_dict()['action_type'] == req_action['action_type']:
                return jsonify(description=f"You have already {'liked' if catch_dup.to_dict()['action_type'] == 1 else 'disliked'} this post"), 405
    action = Action(**req_action)
    add(action)
    commit()
    return jsonify("Success"), 200


@api.route('/action', methods=('GET',))
def action_index():
    actions = Action.query.all()
    json_actions = []
    for action in actions:
        json_actions.append(action.to_dict())
    return jsonify(json_actions)


@api.route('/action/<int:action_id>', methods=("GET",))
def action_read(action_id):
    action = Action.query.get(action_id)
    return jsonify(action.to_dict())


@api.route('/action/<int:action_id>', methods=("DELETE",))
def action_delete(action_id):
    action = Action.query.get(action_id)
    delete(action)
    commit()
    return jsonify(action.to_dict())


# Action CRUD ###########################################


# Category CRUD ###########################################
@api.route('/category', methods=("POST",))
def category_create():
    req_category = request.get_json()
    category = Category(**req_category)
    add(category)
    commit()
    return jsonify(category.to_dict())


@api.route('/category', methods=("GET",))
def category_index():
    categories = Category.query.all()
    json_categories = []
    for category in categories:
        json_categories.append(category.to_dict())

    return jsonify(json_categories)


@api.route('/category/<int:category_id>', methods=("GET",))
def category_read(category_id):
    category = Category.query.get(category_id)
    return jsonify(category.to_dict())


@api.route('/category/<int:category_id>', methods=("DELETE",))
def category_delete(category_id):
    category = Category.query.get(category_id)
    delete(category)
    commit()
    return jsonify(category.to_dict())


# Category CRUD ###########################################

# PICTURE CRUD ###########################################

@api.route('/profile_picture/<int:profile_picture_id>', methods=("GET",))
def profile_picture_read(profile_picture_id):
    # return "sdfdsfhdsuifhius"
    profile_picture = ProfilePicture.query.get(profile_picture_id)

    if profile_picture is None:
        abort(404, "Pic not found")
    else:
        # import pdb;pdb.set_trace()
        # return profile_picture.path
        # return photos.url(profile_picture.path)
        return send_from_directory('storage/profile_pictures', profile_picture.path)
        return jsonify(url.__dict__)


@api.route('/profile_picture', methods=("POST",))
def profile_picture_create():
    user = request.form.get('user_id')
    if 'image' in request.files:
        filename = photos.save(request.files['image'])
        profile_picture = ProfilePicture(user_id=user, path=filename)
        add(profile_picture)
        commit()
        return jsonify(profile_picture.to_dict())
