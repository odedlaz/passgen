from flask import Flask
from os import pardir
from os.path import abspath, dirname, join

base_dir = abspath(join(dirname(__file__), pardir))

static_dir = join(base_dir, "static")
templates_dir = join(base_dir, "templates")

app = Flask(__name__, template_folder=templates_dir)
app.secret_key = 'why would I tell you my secret key?'


from . import api
