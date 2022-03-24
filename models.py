import sqlalchemy.types as types

from abc import ABC

from flask_login import UserMixin
from datetime import datetime


# from app import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


db = SQLAlchemy()


class Timestamp:
    # __tablename__ = 'time_stamp'

    created_at = db.Column(db.DateTime(), default=datetime.now)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.now)


# class ChoiceType(types.TypeDecorator):
#
#     impl = types.String
#
#     def __init__(self, choices, **kw):
#         self.choices = dict(choices)
#         super(ChoiceType, self).__init__(**kw)
#
#     def process_bind_param(self, value, dialect):
#         return [k for k, v in self.choices.items() if v == value][0]
#
#     def process_result_value(self, value, dialect):
#         return self.choices[value]


class CoffeeMachine(db.Model, Timestamp):
    __tablename__ = 'coffee_machine'

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    machine_name = db.Column(db.String())
    caffeine = db.Column(db.Integer)
    # user_id = db.Column(UUID, ForeignKey('user.id'))

    # user = relationship('User')


    def __init__(self, _id, machine_name, caffeine, user_id=None):
        self.id = _id
        self.machine_name = machine_name
        self.caffeine = caffeine
        self.user_id = user_id

    def __repr__(self):
        return f'Coffee Machine : {self.machine_name} with id: {self.id}'


class User(UserMixin, db.Model, Timestamp):
    __tablename__ = 'user'

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def __init__(self, _id, username, email, password):
        self.id = _id
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'USER :: {self.username}'


class Coffee(db.Model, Timestamp):
    __tablename__ = 'coffee'

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    coffee_type = db.Column(db.String(50), nullable=False)
    coffee_mg = db.Column(db.String(20), nullable=False)
    user_id = db.Column(UUID, ForeignKey('user.id'))
    coffee_machine_id = db.Column(UUID, ForeignKey('coffee_machine.id'))

    user = relationship('User')
    coffee_machine = relationship('CoffeeMachine')

    def __init__(self, _id, coffee_type, coffee_mg, user_id, coffee_machine_id):
        self.id = _id
        self.coffee_type = coffee_type
        self.coffee_mg = coffee_mg
        self.user_id = user_id
        self.coffee_machine_id = coffee_machine_id

    def __repr__(self):
        return f'Coffee {self.coffee_type} for {self.user_id}'
