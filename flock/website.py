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


@app.route('/', defaults={'page': 'index'})
@app.route('/<page>')
def show(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)
