# from __future__ import absolute_import, division, print_function, unicode_literals
from flask import *

app = Flask(__name__)
'''
    The cookies are stored in the form of text files on the client's machine. 
    Cookies are used to track the user's activities on the web and reflect some suggestions 
    according to the user's choices to enhance the user's experience.
    
    Cookies are set by the server on the client's machine which will be 
    associated with the client's request to that particular server in all future transactions until the 
    lifetime of the cookie expires or it is deleted by the specific web page on the server.
'''

'''

    set cookies on client's machine: response.setCookie(<title>, <content>, <expiry time>)  
    get cookies from client's machine: request.cookies.get(<title>)  

'''


@app.route('/cookie')
def cookie():
    res = make_response("<h1>Cookie is set.</h1>")
    res.set_cookie("foo", "bar")
    return res


if __name__ == "__main__":
    app.run(debug=True)
