from main import app, db
from flask_smorest import Api
from main.resources.user import blp as user_blueprint
from main.resources.category import blp as category_blueprint
from main.resources.note import blp as note_blueprint

CATEGORIES = db.CATEGORIES
USERS = db.USERS
NOTES = db.NOTES

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Backend lab 2"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"

api = Api(app)

api.register_blueprint(user_blueprint)
api.register_blueprint(category_blueprint)
api.register_blueprint(note_blueprint)


@app.route("/")
def home():
    return "Lab1 IO-04 Vodzinskiy Roman"
