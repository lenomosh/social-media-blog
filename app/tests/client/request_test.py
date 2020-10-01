from app import create_app

from app.tests.fixtures import flask_app, flask_client


def test_reqparse(flask_app):
    @flask_app.route('/hello_world')
    def respond():
        from flask import jsonify
        return jsonify('Hello, World')

    with flask_app.test_client() as cl:
        response = cl.get('/hello_world')
        assert response.status_code == 200
        assert response.json == 'Hello, World'
