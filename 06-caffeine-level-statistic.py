import json
from typing import Dict

from flask import Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

from day_coffee_activity import get_day_coffee_activity
from models import Coffee


def main(query_parameters: Dict, db: SQLAlchemy):
    """
    The function returns caffeine concentration in user's body last 24 hours
    query parameter -- ?user_id=22fa4c17-1dfa-48e4-bd09-1c328318b806
    """
    try:
        last24 = datetime.now() - timedelta(hours=24)
        caffeine_rate = Coffee.query.filter_by(
            user_id=query_parameters['user_id']
        ).filter(
            Coffee.created_at >= last24
        ).filter(
            Coffee.created_at <= datetime.now()
        )
        day_stats = get_day_coffee_activity(caffeine_rate)


        return json.dumps(day_stats), 200

    except Exception as err:
        return Response(f"API call failed: {err}", status=400)
