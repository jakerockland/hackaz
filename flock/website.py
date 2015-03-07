from flock import app

@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"

@app.route("/sqldatabase")
def oh_vip():
    return "Look at this pretty database"
