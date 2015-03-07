from flask import Flask

app = Flask(__name__)

import flock.config
import flock.website
import flock.oauth

if __name__ == "__main__":
    app.run()
