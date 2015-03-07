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


"""
If a user has a Twitter OAuth access token and token secret in their session,
this URL will return a JSON-encoded list of some bullshit that Kuba said...
"""
@app.route('/twitter')
def get_twitter_user_data():
    accountName = request.args['accountName']
    from flock import twitter
    access_token, token_secret = oauth.get_twitter_token()
    if access_token is None and token_secret is None:
        abort(403)
    return jsonify(data=[])
