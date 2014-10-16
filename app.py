import base64
import hashlib
import re
from flask import Flask, render_template, request, flash, jsonify
import itertools
from wtforms import Form, StringField, PasswordField, validators, ValidationError

app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'
url_validation_regex = re.compile(
    r'^((?:http|ftp)s?://)?'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

specials = "8(1~3@4#5$6%7_^}9*0&2"


def validate_url(form, field):
    if not url_validation_regex.match(field.data):
        raise ValidationError("URL is invalid")


class RegistrationForm(Form):
    domain = StringField('Domain', [validators.DataRequired(), validate_url])
    password = PasswordField('Password', [
        validators.DataRequired(), validators.Length(min=4, message="Password is too short.")
    ])


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        secret = generate_password(form.domain.data, form.password.data)
        return render_template('success.html',
                               domain=form.domain.data,
                               password=secret)
    return render_template('index.html',
                           form=form)


def hash(text):
    m = hashlib.sha1()
    m.update(text.encode('utf-8'))
    return m.digest()


def ensureSpecialChars(text):
    new = ""
    for index, char in enumerate(text):
        new += char if index % 7 != 0 else specials[ord(char) % len(specials)]
    return new


def generate_password(domain, password):
    chained = "{0}:{1}".format(domain, password)
    secret_hash = hash(chained)
    text = ensureSpecialChars(base64.b64encode(secret_hash).decode('utf-8'))
    return text[::3]


if __name__ == '__main__':
    app.run(debug=True)
