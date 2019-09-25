from __future__ import absolute_import, print_function, division, unicode_literals
from flask import *

app = Flask(__name__)
app.secret_key = "abc"

'''
The following syntax is used to set the session variable to a specific value on the server.
Session[<variable-name>] = <value>

To remove a session variable, use the pop() method on the session object and mention the variable to be removed.
session.pop(<variable-name>, none)  
'''


@app.route("/")
def home():
    res = make_response("<h4> session variable is set, <a href='/get'>Get Variable</a></h4>")
    session["response"] = "session#1"
    return res


@app.route("/get")
def getVariable():
    if "response" in session:
        s = session["response"]
        return render_template("getsession.html", name=s)


if __name__ == "__main__":
    app.run(debug=True)
