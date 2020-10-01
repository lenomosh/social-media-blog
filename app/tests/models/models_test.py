from app.models import User, Category, Blog
from app.db import add, commit, delete
from app.tests.fixtures import flask_app, dbsession
from app.mailer import send_email
from app import mail


def test_add_user(flask_app, dbsession):
    with flask_app.app_context():
        user_data = {
            "name": "doe",
            "email": "lenomosh@gmail.com",
            "password": "root",
            "username": "john"
        }
        obj = User(**user_data)
        add(obj)
        commit()
        fetched = User.query.filter_by(name='doe').all()
        assert len(fetched) == 1
        assert fetched[0].name == 'doe'
        assert fetched[0].id == 1
        assert fetched[0].username == 'john'
        assert fetched[0].name == 'doe'
        delete_user = User.query.get(1)
        delete(delete_user)
        commit()
        query = User.query.all()
        assert len(query) == 0


def test_add_category(flask_app, dbsession):
    with flask_app.app_context():
        category = {
            "name": "general"
        }
        obj = Category(**category)
        add(obj)
        commit()
        fetched = Category.query.filter_by(name='general').all()
        assert len(fetched) == 1
        assert fetched[0].name == 'general'
        delete_category = Category.query.get(1)
        delete(delete_category)
        commit()
        query = User.query.all()
        assert len(query) == 0


def test_add_blog(flask_app, dbsession):
    with flask_app.app_context():
        category = {
            "name": "general"
        }
        obj = Category(**category)
        add(obj)
        commit()
        user_data = {
            "name": "doe",
            "email": "lenomosh@gmail.com",
            "password": "root",
            "username": "john"
        }
        obj = User(**user_data)
        add(obj)
        commit()

        blog = {
            "user_id": 1,
            "category_id": 1,
            "title": "lorem ipsum",
            "content": "If I am allowed to speak for one minute about the topic of 'one minute pitch', then I would "
                       "say that it is a rather interesting idea. In fact, it's an exciting and stimulating concept; "
                       "if given only 60 seconds to talk about something, how can you possibly do justice to such a "
                       "broad and complex subject? You could start by describing what exactly we mean when we use the "
                       "term \"one minute pitch\", but this term itself raises many questions: in any case, "
                       "the whole thing seems like quite a paradox - after all, what kind of ridiculous situation are "
                       "we being asked to imagine here? As you might expect from someone who has been studying "
                       "philosophy since 2012 (the year he was born), my first response upon hearing that there "
                       "exists an activity known as \"1-minute pitching\" is not positive. But before I voice my "
                       "reservations on this matter, I will try to respond positively with some other potential uses "
                       "of 1-minute pitches. "
        }
        obj = Blog(**blog)
        add(obj)
        commit()
        fetched = Blog.query.filter_by(title="lorem ipsum").all()
        assert len(fetched) == 1
        assert fetched[0].user_id == 1
        assert fetched[0].content == blog['content']
        delete_category = Blog.query.get(1)
        delete(delete_category)
        commit()
        query = Blog.query.all()
        assert len(query) == 0


def test_send_mail(flask_app):
    with flask_app.app_context():
        with mail.record_messages() as outbox:
            send_email(
                '[SOCIAL MEDIA BLOG] Test Email',
                'lenomosh@gmail.com',
                'omondilenox@gmail.com',
                "Test Admin"
            )
