from flask import Flask

app = Flask(_name_)

@app.route("/")

def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)