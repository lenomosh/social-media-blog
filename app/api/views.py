from app import photos
from app.api import api
from flask import request, jsonify, abort, send_from_directory
from app.db import add, commit, delete
from app.models import Blog, Comment, Category, ProfilePicture, User
from flask_jwt_extended import jwt_required, get_jwt_identity


# Blog CRUD ###########################################
@api.route('/blog', methods=['POST'])
@jwt_required
def blog_create():
    data = request.get_json()
    user_id = get_jwt_identity()
    category_id = data['category_id']
    content = data['content']
    title = data['title']
    blog = Blog(user_id=user_id, category_id=category_id, title=title, content=content)
    # import pdb;pdb.set_trace()
    add(blog)
    commit()
    blog = Blog.query.get(blog.id).to_dict()
    return jsonify(blog)


@api.route('/blog', methods=['GET'])
# @jwt_required
def blog_index():
    blogs = Blog.query.all()
    # import pdb;pdb.set_trace()
    json_blogs = []
    for blog in blogs:
        json_blogs.append(blog.to_dict())
    return jsonify(json_blogs)


@api.route('/blog/<int:id>', methods=['DELETE'])
# @jwt_required
def blog_delete(blog_id):
    blog = Blog.query.get(blog_id)

    delete(blog)
    commit()
    return jsonify(blog.to_dict())


@api.route('/blog/<int:blog_id>', methods=['GET'])
# @jwt_required
def blog_read(blog_id):
    blog = Blog.query.get(blog_id)
    if not blog:
        return jsonify(description="Not found"),404

    return jsonify(blog.to_dict())


# Blog CRUD ###########################################

# Comment CRUD ###########################################


@api.route('/comment', methods=['POST'])
@jwt_required
def comment_create():
    req_data = request.get_json()
    comment = Comment(**req_data)
    add(comment)
    commit()
    return comment.to_dict()


@api.route('/comment', methods=['GET'])
# @jwt_required
def comment_index():
    comments = Comment.query.all()
    comment_json = []
    for comment in comments:
        comment_json.append(comment.to_dict())

    return jsonify(comment_json)


@api.route('/comment/<int:comment_id>', methods=("GET",))
# @jwt_required
def comment_read(comment_id):
    comment = Comment.query.get(comment_id)
    return jsonify(comment.to_dict())


@api.route('/comment/<int:comment_id>', methods=("DELETE",))
@jwt_required
def comment_delete(comment_id):
    comment = Comment.query.get(comment_id)
    delete(comment)
    commit()
    return jsonify(comment.to_dict())


# Comment CRUD ###########################################

# Category CRUD ###########################################
@api.route('/category', methods=("POST",))
@jwt_required
def category_create():
    req_category = request.get_json()
    category = Category(**req_category)
    add(category)
    commit()
    return jsonify(category.to_dict())


@api.route('/category', methods=("GET",))
# @jwt_required
def category_index():
    categories = Category.query.all()
    json_categories = []
    for category in categories:
        json_categories.append(category.to_dict())

    return jsonify(json_categories)


@api.route('/category/<int:category_id>', methods=("GET",))
@jwt_required
def category_read(category_id):
    category = Category.query.get(category_id)

    # category['blogs'] = blogs
    return jsonify(category.to_dict())


@api.route('/category/<int:category_id>', methods=("DELETE",))
@jwt_required
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


@api.route('/profile_picture', methods=("POST",))
@jwt_required
def profile_picture_create():
    user_id = get_jwt_identity()
    if 'image' in request.files:
        filename = photos.save(request.files['image'])
        profile_picture = ProfilePicture(user_id=user_id, path=filename)
        add(profile_picture)
        commit()
        return jsonify(profile_picture.to_dict())


@api.route('/my_blogs', methods=("GET",))
@jwt_required
def get_user_blogs():
    user_id = get_jwt_identity()
    blogs = Blog.query.filter_by(user_id=user_id).all()
    json_blogs = []
    for blog in blogs:
        json_blogs.append(blog.to_dict())

    return jsonify(json_blogs)


@api.route('/user_profile/<int:user_id>')
@jwt_required
def load_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(description="User not found"), 404
    user_clone = user.to_dict(only=("name", "blogs", "id", "CREATED_AT", "profile_picture.id","username",))
    return jsonify(user_clone)
