# standard library imports
import os
import uuid
import json
import httplib2

# Flask and web server imports
from flask import render_template, redirect, url_for, abort, request, flash, jsonify
from jinja2 import TemplateNotFound
from flask.ext.assets import Environment, Bundle

# custom module imports
from flock import app

@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"

@app.route("/about")
def oh_vip():
    return "About page bby"
