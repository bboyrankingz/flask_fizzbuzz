import json

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/fizzbuzz/")
def fizzbuzz():
    string1 = request.args.get('string1', 'fizz')
    string2 = request.args.get('string2', 'buzz')
    int1 = request.args.get('int1', 3)
    int2 = request.args.get('int2', 5)
    limit = request.args.get('limit', 100)
    fizzbuzz = [(string1 if i % int(int1) == 0 else "") + (string2 if i % int(int2) == 0 else "") or i for i in
                xrange(1, int(limit) + 1)]
    return json.dumps(fizzbuzz)


if __name__ == "__main__":
    app.run()
