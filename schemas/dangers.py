async def danger_entity(danger: dict) -> dict:
    return {
        'name': danger['name'],
        'description': danger['description'],
        'dangerLevel': danger['danger_level'],
        'coordinates': danger['coordinates'],
    }
