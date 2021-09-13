import os

from flask import Flask, render_template
from flask_migrate import Migrate

from models.database import db
from views.users import users_app

app = Flask(__name__)
app.register_blueprint(users_app, url_prefix="/users")

SQLALCHEMY_DATABASE_URI = os.getenv("DB_CONN_URI", "postgresql+psycopg2://user:password@localhost:5432/users")
app.config.update(
    SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/', endpoint='index')
def get_index():
    return render_template('index.html')


@app.route('/about/', endpoint='about')
def get_about():
    return render_template('about.html')
