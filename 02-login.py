import bcrypt

from uuid import uuid4
from flask import Response
from flask_httpauth import HTTPBasicAuth
from flask_login import login_user

from models import User

auth = HTTPBasicAuth


def main(data_to_login, db) -> Response:

    # try:

    user = User.query.filter_by(email=data_to_login['email'].lower()).first()
    password = user.password
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(data_to_login['password'].encode(), salt)

    valid = bcrypt.checkpw(password.encode(), hash)
    print(valid)
    # valid = bcrypt.hashpw(data_to_login['password'].encode(), user.password.encode())
    if valid:
        login_user(user)
        print('ehehheheehehe')
        return Response(f'User {user.username} is successfully authenticated', status=200)

    # except Exception as err:
    #     return Response(f"API call failed: {err}", status=400)
