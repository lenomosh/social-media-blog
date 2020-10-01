from app.tests.fixtures import flask_app, flask_client

def test_app_creates(flask_app):
    assert flask_app


def test_app_healthy(flask_app, flask_client):
    with flask_client:
        resp = flask_client.get('/api/healthy')
        assert resp.status_code == 200
        assert resp.is_json
        assert resp.json == 'healthy'