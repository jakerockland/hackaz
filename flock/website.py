from flock import app

@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"
