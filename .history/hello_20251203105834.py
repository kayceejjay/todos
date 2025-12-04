from flask import Flask

app = Flask(name)

@app.route("/")

def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)