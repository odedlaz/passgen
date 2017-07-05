import os
from flask import render_template, send_from_directory

from passgen import app

dirname = os.path.dirname(os.path.realpath(__file__))
assets_dir = os.path.join(dirname, "assets")


@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory(assets_dir, path)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
