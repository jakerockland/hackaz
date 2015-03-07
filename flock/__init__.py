from flask import Flask

app = Flask(__name__)

import website

if __name__ == "__main__":
    app.run()
