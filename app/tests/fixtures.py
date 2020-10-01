
import pytest

from app import create_app


@pytest.fixture
def flask_app():
    return create_app('test')


@pytest.fixture
def flask_client(flask_app):
    return flask_app.test_client()


@pytest.fixture
def dbsession(flask_app):
    from app.db import db
    with flask_app.app_context():
        db.create_all()
        yield db
        db.drop_all()
        db.session.commit()

