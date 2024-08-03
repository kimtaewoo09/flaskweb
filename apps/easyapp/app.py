from flask import Flask, render_template, url_for, redirect, request
from email_validator import validate_email
app = Flask(__name__)

app.config["SECRET_KEY"]=b'\xc3\xe0\x10\xe0\x16>S_g\xcb0\xb0h\xcf."'

@app.route("/")
def index():
    return 'Hello, flaskweb'

@app.route("/hello/<name>",methods=["GET"],endpoint='hello')
def hello(name):
    return f"hello!! {name}!!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html",name=name)
#문의 폼
@app.route("/contact")
def contact():
    return render_template("contact.html")

#문의 완료 폼
@app.route("/contact_complete", methods=["GET","POST"])
def contact_complete():
    if request.method == "POST":
        username=request.form["username"]
        email=request.form["email"]
        description=request.form["description"]

        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")

with app.test_request_context():
    print(url_for("index"))
    print(url_for("index"))
    print(url_for("show_name",name='chilty',page=1))