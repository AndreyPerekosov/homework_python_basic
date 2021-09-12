import os
from models.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

    posts = db.relationship("Post", backref="user")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}), "
            f"name={self.name!r}, username={self.username!r},"
            f"email={self.email!r}"
        )

    def __repr__(self):
        return str(self)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False, default="", server_default="")
    body = db.Column(db.Text, nullable=False, default="", server_default="")

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}), "
            f"title={self.title!r}, user_id={self.user_id}"

        )

    def __repr__(self):
        return str(self)

