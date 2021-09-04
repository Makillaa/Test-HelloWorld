from flask import Flask, render_template
# import hello

application = Flask(__name__)

@application.route("/")
def hellopage():
    return "Hi"
  
if __name__ == "__main__":
    application.run()
