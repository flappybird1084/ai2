import os

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Riris_c0de'
from app import views
