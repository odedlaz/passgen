from flask import Flask

app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'

from . import api
