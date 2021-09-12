from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.exceptions import NotFound

from models import User
from models.database import db

users_app = Blueprint("users_app", __name__)


@users_app.route("/", endpoint="list")
def get_users_list():
    users = User.query.all()
    return render_template("users/list.html", users=users)


@users_app.route("/<int:user_id>/", endpoint="detail")
def get_user(user_id: int):
    user = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        raise NotFound(f"No user for id {user_id}")
    posts = user.posts
    return render_template("users/detail.html", user=user, posts=posts)
