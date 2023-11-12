async def danger_entity(danger: dict) -> dict:
    return {
        'name': danger['name'],
        'description': danger['description'],
        'coordinates': danger['coordinates'],
        'date_time': str(danger['date_time']),
    }
