"""
Simple flask template example
"""

# from flask import *
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "<html><body><h1>Hello User.!</h1></body></html>"
#
# if __name__ == "__main__":
#     app.run(debug=True)

'''
    flask template rendering example
    flask templates need to kept under the templates directory else
    error will be encountererd
'''

# from __future__ import absolute_import, unicode_literals, print_function, division
# from flask import *
# app = Flask(__name__)
# @app.route('/')
# def message():
#     return render_template('message.html')
# if __name__ == "__main__":
#     app.run(debug=True)

'''
    template rendering using flask delimiters.
    Jinga 2 template engine provides some delimiters which can be used 
    in the HTML to make it capable of dynamic data representation.
    
    The jinga2 template engine provides the following delimiters to escape from the HTML.
        1. {% ... %} for statements
        2. {{ ... }} for expressions to print to the template output
        3. {# ... #} for the comments that are not included in the template output
        4. # ... ## for line statements
'''

#from __future__ import absolute_import, unicode_literals, print_function, division
# from flask import *
#
# app = Flask(__name__)
# @app.route('/user/<uname>')
# def message(uname):
#     return render_template('message.html',name=uname)
# if __name__ == "__main__":
#     app.run(debug=True)

#Embedding python statements in html

from flask import *
app = Flask(__name__)

@app.route("/mul/<num>")
def print_num(num):
    return render_template("message.html",num=num)

if __name__ == "__main__":
    app.run(debug = True)