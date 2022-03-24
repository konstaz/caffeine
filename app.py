import flask

from flask import Flask, request
from flask_migrate import Migrate
from flask_login import LoginManager, login_required
from models import User, db
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
app.config['SECRET_KEY'] = config.SECRET_KEY
login_manager = LoginManager()
login_manager.init_app(app)


examples = [
    "01-signup",
    "02-login",
    "03-create-coffee-machine",
    "04-coffee-consumption-history",
    "05-coffee-purchase",
    "06-caffeine-level-statistic"
]


@app.route("/")
def show_list():  # just a list of endpoints on home page
    """
    The list of available functions
    """
    body = ""
    for example in examples:
        body += f'<a href="/{example}">{example}</a><br>'
    return body


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


@app.route("/", methods=['POST'])
def login():
    """
    The function responsible for login
    {
    "email":"email@email.email",
    "password":"password"
    }
    """
    return __import__('02-login').main(request.get_json(), db)


@app.route("/<example>", methods=["GET", "POST", "PUT"])  # @login_required
def run_example(example=None):
    """
    The function responsible to launch main function of python files
    whose names are in the list examples mentioned above
    """

    data = request.args if not request.get_json() else request.get_json()
    # I know I could validate between types of requests either POST or GET or PUT
    # when executing function but here I just wanted to complete it in one row
    if example not in examples:
        flask.abort(404, "Example does not exist")
    return __import__(example).main(data, db)


if __name__ == '__main__':
    app.debug = True
    app.run()
