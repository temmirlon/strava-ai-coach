from app.activities.schemas import Activity

def map_strava_activity(data: dict) -> Activity:
    return Activity(
        external_id= str(data["id"]),
        provider= "strava",
        name=data["name"],
        sport_type=data["sport_type"],
        distance_meters=data["distance"],
        duration_seconds=data["moving_time"],
        average_heart_rate=data.get("average_heartrate"),
        max_heart_rate=data.get("max_heartrate"),
        elevation_gain_meters=data.get("total_elevation_gain"),
    )