from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__,template_folder="templates")

@app.route("/home")
def home():
    value=request.args.get('howareu')
    return render_template("home.html",val=value)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)


