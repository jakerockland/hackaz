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
from flock import app, oauth, config, espresso


"""
This function configures the application container with variables from the
configuration in secrets.json as well as the static assets (JavaScript and CSS)
that must be served to the visitor of the web site.
"""
def configure_application():
    assets = Environment(app)
    assets.debug = app.debug

    assets.register('leche_js', espresso.leche_js)

configure_application()


"""
This URL handler defaults to serving the 'index.html' page renderred using
the Jinja2 templating engine bundled with the Flask framework.

In addition to setting the default homepage to 'index.html', it provides a
default fallback for any URL a user attempts to visit. If a user visits a page
that doesn't have a defined URL route. If the HTML file exists, it will serve
the renderred version of the file. Otherwise, the function will serve a 404
'Not Found' error.
"""
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
    from flock.teacup import twitter
    access_token, token_secret = oauth.get_twitter_token()
    if access_token is None and token_secret is None:
        abort(403)
    return redirect(url_for('suggest'))
    # return jsonify(names=[],tags=[],profs=[])
