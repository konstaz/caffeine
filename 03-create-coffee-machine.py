import json
from uuid import uuid4
from flask import Response
from flask_sqlalchemy import SQLAlchemy

from models import CoffeeMachine


def main(data_to_store: json, db: SQLAlchemy) -> Response:
    """
    The function creates a coffee machine with info about it
    {
    "machine_name":"machine_name",
    "caffeine":"caffeine"
    }
    """
    try:

        coffee_machine = CoffeeMachine(
            _id=uuid4(),
            machine_name=data_to_store['machine_name'],
            caffeine=data_to_store['caffeine']
        )
        db.session.add(coffee_machine)
        db.session.commit()

        return Response(f"Coffee Machine {str(data_to_store['machine_name'])} is successfully created", status=200)

    except Exception as err:
        return Response(f"API call failed: {err}", status=400)