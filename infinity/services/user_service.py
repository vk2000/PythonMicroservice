from  flask import Flask, jsonify,flash,request,redirect,url_for,render_template,send_from_directory
import yaml
import os
import pandas as pd
from pathlib import Path
import json


# instantiate the app
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16* 1024 * 1024
# set config
# app.config.from_object('project.config.DevelopmentConfig')



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users', methods=['GET', 'POST'])
def users():
    with open('../infinity/services/data/users.json') as data:
        return jsonify(json.load(data))


@app.route('/user', methods=['GET', 'POST'])
def user():
    post_data = request.get_json(force=True)
    userid =  post_data["user_id"]
    with open('../infinity/services/data/users.json') as data_src:
        data =  json.load(data_src)
        user = data['users'][userid]
    return jsonify(user)

@app.route('/user_get/<user_id>', methods=['GET'])
def user_get(user_id):
    with open('../infinity/services/data/users.json') as data_src:
        data =  json.load(data_src)
        user = data['users'][user_id]
    return jsonify(user)

#if __name__ == '__main__':
#    app.run(host='0.0.0.0')

