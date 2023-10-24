from flask import Flask

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = b"secret key"

from app import views