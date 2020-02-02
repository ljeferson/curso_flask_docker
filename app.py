from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def showname():
    name = request.args.get("name")
    return f"Name: {name}"

@app.route("/name/<name>")
def showname_param(name):
    return name

app.run(debug=True, port=3000, host="0.0.0.0")