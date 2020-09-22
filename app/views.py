from flask import current_app, make_response, jsonify

app = current_app


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
