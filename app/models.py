from app.db import (
    String,
    Column,
    TIMESTAMP,
    BigInteger,
    Text,
    ForeignKey,
    Model,
    Relationship)
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, decode_token, create_refresh_token
from datetime import timedelta


class Common(SerializerMixin):
    id = Column(
        BigInteger,
        primary_key=True
    )
    CREATED_AT = Column(
        TIMESTAMP,
        default=datetime.utcnow()
    )
    UPDATED_AT = Column(
        TIMESTAMP,
        nullable=True
    )


class Category(Common, Model):
    __tablename__ = 'categories'
    name = Column(
        String(50),
        nullable=False
    )
    # serialize_only = (
    #     'blogs.content',
    #     'blogs.author.name',
    #     "blogs.author.profile_picture.id",
    #     "id",
    #     "name",
    #     "blogs.comments"
    #     ,)


class Blog(Model, Common):
    __tablename__ = 'blogs'
    content = Column(
        Text,
        nullable=False
    )
    user_id = Column(
        BigInteger,
        ForeignKey('users.id'),
        nullable=False
    )
    category_id = Column(
        BigInteger,
        ForeignKey('categories.id'),
        nullable=False
    )
    author = Relationship(
        'User',
        backref='blogs',
        lazy='subquery',
        uselist=False
    )
    category = Relationship(
        'Category',
        backref='blogs',
        lazy='subquery',
        uselist=False
    )
    comments = Relationship(
        'Comment',
        lazy='subquery'
    )
    #
    # def likes(self):
    #     return self.query.filter

    serialize_only = (
        'category.name',
        'author.name',
        'author.profile_picture.id',
        'author.id',
        "id",
        "content",
        "comments.author.name",
        "comments.author.profile_picture.id",
        "comments.author.id",
        "comments.CREATED_AT",
        "comments.content",
        "comments.id"

        ,)


class User(Model, Common, UserMixin):
    __tablename__ = 'users'
    name = Column(
        String(50),
        nullable=False
    )
    username = Column(
        String(50),
        nullable=False,
        unique=True
    )
    about = Column(
        String(250),
        nullable=True
    )
    email = Column(
        String(100),
        nullable=False,
        unique=True
    )
    password = Column(
        String,
        nullable=False
    )
    profile_picture = Relationship(
        "ProfilePicture",
        lazy='subquery',
        uselist=False
    )

    def generate_refresh_token(self, expiration=30):
        return create_refresh_token(identity=self.id, expires_delta=timedelta(minutes=expiration))

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def generate_auth_token(self, expiration=30):
        return create_access_token(
            identity=self.id,
            expires_delta=timedelta(minutes=expiration))

    @staticmethod
    def verify_auth_token(token):
        try:
            data = decode_token(token)
        except:
            return
        return User.query.get(data['id'])


class Comment(Model, Common):
    __tablename__ = 'comments'
    content = Column(
        Text,
        nullable=False
    )
    pitch_id = Column(
        BigInteger,
        ForeignKey('blogs.id'),
        nullable=False
    )
    user_id = Column(
        BigInteger,
        ForeignKey('users.id'),
        nullable=False
    )
    author = Relationship(
        "User",
        backref="comments",
        lazy='subquery'
    )
    serialize_only = (
        "id",
        "CREATED_AT",
        "content",
        "author.name",
        "author.profile_picture.id"
        ,)


class ProfilePicture(Common, Model):
    __tablename__ = 'profile_pictures'
    path = Column(
        String(256),
        nullable=False
    )
    user_id = Column(
        BigInteger,
        ForeignKey('users.id'),
        nullable=False
    )


class NewsLetter(Common,Model):
    __tablename__ = 'newsletters'
    user_id = Column(
        BigInteger,
        ForeignKey('users.id'),
        unique=True,
        nullable=False
    )
