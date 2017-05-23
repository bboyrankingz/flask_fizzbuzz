import json

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/fizzbuzz/")
def fizzbuzz():
    fizzbuzz = [("fizz" if i % 3 == 0 else "") + ("buzz" if i % 5 == 0 else "") or i for i in xrange(1, 101)]
    return json.dumps(fizzbuzz)

if __name__ == "__main__":
    app.run()
