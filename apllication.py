from flask import Flask, render_template
import os
import hello
application = Flask(__name__)

@application.route("/hello")
def hellopage():
    return hello
  
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)
