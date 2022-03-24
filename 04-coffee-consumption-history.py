import json
from flask import Response
from flask_sqlalchemy import SQLAlchemy

from models import Coffee


def main(query_parameters: dict, db: SQLAlchemy):
    """
    The function returns full coffee consumption history of user
    query parameter -- ?user_id=22fa4c17-1dfa-48e4-bd09-1c328318b806
    """
    try:

        coffee_history = Coffee.query.filter_by(user_id=query_parameters['user_id'])
        coffies = []
        for coffee in coffee_history:
            cup_of_coffee = {
                'id': str(coffee.id),
                'coffee_type': coffee.coffee_type,
                'coffee_mg': coffee.coffee_mg,
                'coffee_machine_id': coffee.coffee_machine_id
            }
            coffies.append(cup_of_coffee)
        return json.dumps(coffies), 200

    except Exception as err:
        return Response(f"API call failed: {err}", status=400)