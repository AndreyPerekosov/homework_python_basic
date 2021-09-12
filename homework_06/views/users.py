import logging
from flask import Blueprint, request, render_template, redirect, url_for
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError

from models import User, Post
from models.database import db

log = logging.getLogger(__name__)

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
    return render_template("users/detail.html", user=user)


@users_app.route("/<int:user_id>/add", methods=["GET", "POST"], endpoint="add")
def create_post(user_id: int):
    user = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        raise NotFound(f"No user for id {user_id}")
    if request.method == "GET":
        return render_template("users/add.html", user=user)
    post_title = request.form.get("post-title")
    post_body = request.form.get("post-body")
    if not post_title or not post_body:
        raise BadRequest("Please fill in title and body")
    post = Post(title=post_title, body=post_body)
    user.posts.append(post)
    try:
        db.session.commit()
    except IntegrityError:
        log.exception("Could not add the post, got integrity error")
        db.session.rollback()
    except DatabaseError:
        log.exception("Could not add the post, got database error")
        db.session.rollback()
        raise InternalServerError("Error adding the post")
    return redirect(url_for("users_app.detail", user_id=user.id))
