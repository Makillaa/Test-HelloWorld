from flask import Flask
import hello

application = Flask(__name__)


@application.route("/")
def root():
    return hello
  

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)
