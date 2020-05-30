from .. import db


class Board(db.Model):
    """ Board Model for storing board related details """
    __tablename__ = "board"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

class Task(db.Model):
    """ Task Model for storing task related details """
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    board_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.String(255), nullable=True)
    label = db.Column(db.String(255), nullable=True)
    desc = db.Column(db.String(255), nullable=True)
    creation_date = db.Column(db.DateTime, nullable=False)
    update_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)
    is_archived = db.Column(db.Boolean, nullable=False, default=False)

class Status(db.Model):
    """ Status Model for storing task status related details """
    __tablename__ = "status"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

class Label(db.Model):
    """ Label Model for storing task label related details """
    __tablename__ = "label"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

class Priority(db.Model):
    __tablename__ = "priority"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

class User(db.Model):
    """User Model for storing user related details"""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)





    # email = db.Column(db.String(255), unique=True, nullable=False)
    # registered_on = db.Column(db.DateTime, nullable=False)
    # admin = db.Column(db.Boolean, nullable=False, default=False)
    # public_id = db.Column(db.String(100), unique=True)
    # username = db.Column(db.String(50), unique=True)
    # password_hash = db.Column(db.String(100))