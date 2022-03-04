from flask import Flask
app=Flask(__name__)
@app.route("/home/<name>")
def home(name):
    return "<h1> Good Morning %s </h1>" % name

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

