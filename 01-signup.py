import bcrypt

from uuid import uuid4
from flask import Response
from flask_sqlalchemy import SQLAlchemy

from models import User


def main(data_to_store: dict, db: SQLAlchemy) -> Response:
    """
    The function for signing up
    {
    "username":"username",
    "email":"email@email.email",
    "password":"password"
    }
    """
    try:
        print(data_to_store)
        hashed_password = bcrypt.hashpw(data_to_store['password'].encode(), bcrypt.gensalt())

        user = User(
            _id=uuid4(),
            username=data_to_store['username'],
            email=data_to_store['email'].lower(),
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()

        return Response(f"User {str(data_to_store['username'])} is successfully created", status=200)

    except Exception as err:
        return Response(f"API call failed: {err}", status=400)
