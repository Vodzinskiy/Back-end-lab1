from main import app, db
from flask_smorest import Api
from main.resources.user import blp as user_blueprint
from main.resources.category import blp as category_blueprint
from main.resources.note import blp as note_blueprint


app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Backend lab 2"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.db.init_app(app)

api = Api(app)

with app.app_context():
    db.db.create_all()

api.register_blueprint(user_blueprint)
api.register_blueprint(category_blueprint)
api.register_blueprint(note_blueprint)


@app.route("/")
def home():
    return "Lab1 IO-04 Vodzinskiy Roman"
