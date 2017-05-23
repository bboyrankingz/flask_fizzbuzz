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
    fizzbuzz = ["{}{}".format(word_or_empty(i, int1, string1), word_or_empty(i, int2, string2)) or i for i in
                xrange(1, int(limit) + 1)]
    return json.dumps(fizzbuzz)


def word_or_empty(i, number, word):
    return word if i % int(number) == 0 else ""


if __name__ == "__main__":
    app.run()
