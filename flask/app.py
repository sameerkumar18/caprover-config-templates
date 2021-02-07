# -*- coding: utf-8 -*-

import flask

app = flask.Flask(__name__)


@app.route('/test', methods=['GET'])
def home():
    print("API is Working")

    return "API is Working"
