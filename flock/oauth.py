# Flask and web server imports
from flask import session, url_for, request, flash, redirect, abort, jsonify
from flask_oauthlib.client import OAuth

# custom module imports
from flock import app, config


oauth = OAuth(app) # create OAuth container

# create a container with Twitter configuration
twitter_config = config.oauth.get('twitter', {})
twitter_auth = oauth.remote_app(
    "twitter",
    access_token_method='get',
    **twitter_config
)


"""
Return a URL to redirect the user to after authenticating with a third-party
application like Facebook or Twitter.
"""
def get_next_url():
    return request.args.get('next') or request.referrer or None


"""
Retrieve Twitter access tokens from the user's session. Uses Flask session
as the storage backend (data stored as an ecrypted cookie in the browser).
"""
@twitter_auth.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token',(None, None))


"""
Provide a URL endpoint that allows a user to log in to Twitter to authorize
access to their account via OAuth. This handler returns a redirect to the
Twitter web site.
"""
@app.route('/login')
def login():
    return twitter_auth.authorize(callback=url_for('oauth_authorized',
        next=request.args.get('next') or request.referrer or None))


"""
Provide a URL endpoint that the user will visit after authorizing Flock
as a client application for their Twitter account.
"""
@app.route('/oauth-authorized')
@twitter_auth.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['twitter_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    session['twitter_user'] = resp['screen_name']

    flash('You were signed in as %s' % resp['screen_name'])
    return redirect(next_url)
