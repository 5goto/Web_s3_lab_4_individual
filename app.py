from flask import Flask, url_for, request
from controller.get_reader_page import *

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def reader_table():
    if request.method == "POST":
        pars = request.form.to_dict()
        return get_simple_request(pars['min_days'], pars['max_year'])
    else:
        return get_simple_request()


if __name__ == '__main__':
    app.run()
