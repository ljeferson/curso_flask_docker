from flask import Flask, request, Response

app = Flask(__name__)



@app.route("/home")
def home():
    return Response("Home Page", 200, {})


@app.route("/")
def showname():
    name = request.args.get("name")
    return f"Name: {name}"

@app.route("/name")
@app.route("/name/<name>")
def showname_param(name = None):
    if name:
        return name
    return "Nome não foi preenchido!"

app.run(debug=True, port=3000, host="0.0.0.0")