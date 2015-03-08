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
    access_token_method='GET',
    **twitter_config
)


"""
Return a URL to redirect the user to after authenticating with Twitter
"""
def get_next_url():
    return request.args.get('next') or request.referrer or None


"""
Retrieve Twitter access tokens from the user's session. Uses Flask session
as the storage backend (data stored as an ecrypted cookie in the browser).
"""
@twitter_auth.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token', (None, None))


"""
Provide a URL endpoint that allows a user to log in to Twitter to authorize
access to their account via OAuth. This handler returns a redirect to the
Twitter web site.
"""
@app.route('/login/twitter')
def login_twitter():
    return twitter_auth.authorize(
        callback=url_for(
            'oauth_authorized_twitter',
            next=get_next_url(),
            _external=True
        )
    )


"""
Provide a URL endpoint that the user will visit after authorizing Flock
as a client application for their Twitter account.
"""
@app.route('/oauth-authorized/twitter')
@twitter_auth.authorized_handler
def oauth_authorized_twitter(authentication):
    if authentication is None:
        flash(u'We did not receive authorization for your Twitter account.')
    else:
        flash(u'Successfully authenticated with Twitter.')
        session['twitter_token'] = (
            authentication['oauth_token'],
            authentication['oauth_token_secret']
        )

    return redirect(request.args.get('next') or '/')
