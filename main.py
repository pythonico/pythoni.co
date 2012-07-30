from datetime import date
import os

from flask import send_from_directory
from flask import Flask
from flask import render_template
from flask import request
from flask import current_app
from flask import redirect

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    return render_template(
        "index.html",
	    year=date.today().year,
    )

if __name__ == "__main__":
    app.debug = True
    app.run(port=5001)
