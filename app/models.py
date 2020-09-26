from app.db import (
    String,
    Column,
    TIMESTAMP,
    BigInteger,
    Integer,
    Text,
    ForeignKey,
    Model,
    Relationship)
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin


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
    serialize_only = (
        'pitches.content',
        'pitches.author.name',
        "pitches.author.profile_picture.id",
        "id",
        "name"
        ,)


class Pitch(Model, Common):
    __tablename__ = 'pitches'
    content = Column(
        String(1000),
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
        backref='pitches',
        lazy=True,
        uselist=False
    )
    category = Relationship(
        'Category',
        backref='pitches',
        lazy=True,
        uselist=False
    )
    actions = Relationship(
        'Action',
        lazy=True,
    )
    comments = Relationship(
        'Comment',
        lazy=True
    )
    def likes(self):
        return self.query.filter
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
        lazy=True,
        uselist=False
    )


class Comment(Model, Common):
    __tablename__ = 'comments'
    content = Column(
        Text,
        nullable=False
    )
    pitch_id = Column(
        BigInteger,
        ForeignKey('pitches.id'),
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
        lazy=True
    )
    serialize_only = (
        "id",
        "CREATED_AT",
        "content",
        "author.name",
        "author.profile_picture.id"
        ,)


class Action(Common, Model):
    __tablename__ = 'actions'
    user_id = Column(
        BigInteger,
        ForeignKey('users.id'),
        nullable=False
    )
    pitch_id = Column(
        BigInteger,
        ForeignKey('pitches.id'),
        nullable=False
    )
    action_type = Column(
        Integer,
        nullable=False
    )


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
