from flask import Flask
app = Flask(__name__)

greeting1 = "Hello World!"
greeting2 = "in NoteIt!"

@app.route("/")
def home():
    return f"{greeting1} You are {greeting2}"
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
