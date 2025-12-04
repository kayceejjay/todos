from_flask_import Flask
app = Flask(_name_)
@app.route("/")
def_hello_world():
    return "<p>Hello, World!</p>"