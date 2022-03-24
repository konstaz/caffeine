from datetime import datetime, timedelta
from typing import List

day_stats = []
time_range = [int((datetime.now() - timedelta(hours=time)).strftime("%H")) for time in range(24)]



def get_day_coffee_activity(caffeine_rate: List) -> List:

    caffeine_info = [0]  # have done so cause list is mutable and couldn't something more efficient
    time_range.reverse()
    for coffee in caffeine_rate:

        for hour in time_range:

            if int(coffee.created_at.strftime("%H")) == hour:
                caffeine_info[0] = 100
                cup_of_coffee = {
                    'coffee_type': coffee.coffee_type,
                    'coffee_machine_id': coffee.coffee_machine_id,
                    'caffeine_concentration': caffeine_info,
                    'time_of_purchase': coffee.created_at.strftime("%H:%M")
                }
            else:
                caffeine_info[0] = caffeine_info[0] - 10
                cup_of_coffee = {
                    'coffee_type': '',
                    'coffee_machine_id': '',
                    'caffeine_concentration': caffeine_info[0] if caffeine_info[0] > 0 else 0,
                    'time_of_purchase': ''
                }

            day_stats.append(cup_of_coffee)

    return day_stats[:24]