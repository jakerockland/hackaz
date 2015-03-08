from flask import Flask

app = Flask(__name__)

import flock.config
import config
import flock.website
import flock.oauth
