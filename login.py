from __future__ import absolute_import, print_function, division, unicode_literals
from flask import *

app = Flask(__name__)

@app.route("/error")
def error():
    return "<h1>Sorry we encountered some error</h1>"

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
    if password == "deepmind":
        resp = make_response(render_template("success.html"))
        resp.set_cookie('email', email)
        return resp
    else:
        return redirect(url_for("error"))

@app.route("/viewprofile")
def view_profile():
    email = request.cookies.get("email")
    resp = make_response(render_template("viewprofile.html", name=email))
    return resp

if __name__ == "__main__":
    app.run(debug=True)
