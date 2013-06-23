from flask import jsonify
from flask import request

from app import app


@app.route('/api', methods=['GET', 'POST'])
def hello():
    if request.query_string:
        app.logger.info('query string: %s' % request.query_string)
    if request.form:
        app.logger.info('parameters: %s' % request.form)
    return jsonify(app.config['API_RESPONSE'])
