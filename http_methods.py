# from flask import *
#
# app = Flask(__name__)
#
# @app.route('/login', methods=["GET"])
# def login():
#     uname = request.args.get('uname')
#     password = request.args.get("pwd")
#     if uname=="rohit" and password=="google":
#         return "hello %s" % uname
#
# if __name__ == "__main__":
#     app.run(debug=True)

from __future__ import absolute_import, division, print_function, unicode_literals

from flask import *
app = Flask(__name__)

@app.route("/login",methods=["POST"])
def login():
    uname = request.form("uname")
    password = request.form("pwd")
    if uname=="rohit" and password == "google":
        return "hello %s"%uname
    else:
        return "User not found. Error.!"