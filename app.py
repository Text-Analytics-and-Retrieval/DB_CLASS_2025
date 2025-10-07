from flask import Flask, render_template

from api.api import *  # noqa I001s
from api.sql import *  # noqa I001
from backstage.views.analysis import *  # noqa I001
from backstage.views.manager import *  # noqa I001
from bookstore.views.store import *  # noqa I001
from link import *  # noqa I001

## Flask-Login : 確保未登入者不能使用系統
app = Flask(__name__)
app.secret_key = "Your Key"

app.register_blueprint(api, url_prefix="/")  # noqa F405
app.register_blueprint(store, url_prefix="/bookstore")  # noqa F405
app.register_blueprint(analysis, url_prefix="/backstage")  # noqa F405
app.register_blueprint(manager, url_prefix="/backstage")  # noqa F405

login_manager.init_app(app)  # noqa F405


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.secret_key = "Your Key"
    app.run()
