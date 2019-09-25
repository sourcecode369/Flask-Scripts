from __future__ import absolute_import, unicode_literals, print_function, division
from flask import *

app = Flask(__name__)


@app.route("/")
def get_customer_data():
    return render_template("customer_info.html")


@app.route('/success', methods=["POST", "GET"])
def print_data():
    if request.method == "POST":
        result = request.form
        return render_template(
            "result_data.html", result=result
        )


if __name__ == "__main__":
    app.run(debug=True)
