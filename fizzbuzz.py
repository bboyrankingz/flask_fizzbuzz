import json

from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/fizzbuzz/")
def fizzbuzz():
    string1 = request.args.get('string1', 'fizz')
    fizzbuzz = [(string1 if i % 3 == 0 else "") + ("buzz" if i % 5 == 0 else "") or i for i in xrange(1, 101)]
    return json.dumps(fizzbuzz)

if __name__ == "__main__":
    app.run()
