from flask import render_template, send_from_directory

from passgen import app, static_dir


@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory(static_dir, path)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
