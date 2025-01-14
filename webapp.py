import os
import json

from flask import Flask, make_response, redirect, url_for
from flask import request, jsonify, render_template

from covid_efnd import CovidEfnd

os.environ["FLASK_RUN_HOST"] = "0.0.0.0"

app = Flask(__name__)