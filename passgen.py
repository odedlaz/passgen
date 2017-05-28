import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'

assets_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                          "assets")


@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory(assets_dir, path)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)
