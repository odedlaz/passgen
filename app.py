from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'


@app.route('/assets/<path:path>')
def send_js(path):
    return send_from_directory('assets', path)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)
