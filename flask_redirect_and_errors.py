from __future__ import absolute_import, unicode_literals, print_function, division
from flask import *
'''
Flask class provides the redirect() function which redirects the user to some specified URL with the specified status code.

An HTTP status code is a response from the server to the request of the browser. When we visit a website,
a request is sent to the server, and the server then responds to the browser's request with a three-digit code:
the HTTP status code. This status code also represents the error.
'''
'''
    Flask.redirect(<location>,<status-code>, <response> )  
'''

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/validate',methods=["POST"])
def validate():
    if request.method == "POST" and request.form["pass"]=="deepmind":
        return redirect(url_for("success"))
    return redirect(url_for("login"))

@app.route('/success')
def success():
    return "logged successfully"

if __name__ == "__main__":
    app.run(debug=True)