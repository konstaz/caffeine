import json
from uuid import uuid4
from flask import Response
from flask_sqlalchemy import SQLAlchemy

from models import Coffee


def main(data_to_store: json, db: SQLAlchemy) -> Response:
    """
    The function responsible for coffee purchasing
    {
    "coffee_type":"coffee_type",
    "coffee_mg":"coffee_mg",
    "user_id":"user_id",
    "coffee_machine_id":"coffee_machine_id"
    }
    """
    try:
        coffee = Coffee(
            _id=uuid4(),
            coffee_type=data_to_store['coffee_type'],
            coffee_mg=data_to_store['coffee_mg'],
            user_id=data_to_store['user_id'],
            coffee_machine_id=data_to_store['coffee_machine_id']
        )
        db.session.add(coffee)
        db.session.commit()

        return Response(
            f"{data_to_store['coffee_type']} is purchased by {data_to_store['user_id']} from {data_to_store['coffee_machine_id']}",
            status=200
        )

    except Exception as err:
        return Response(f"API call failed: {err}", status=400)