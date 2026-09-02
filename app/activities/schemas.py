from pydantic import BaseModel

# short version of activity
class ActivitySummary(BaseModel):
    id: int
    name: str
    sport_type: str
    distance_km: float
    moving_time_minutes: int

# detailed version of activity
class ActivityDetail(ActivitySummary):
    average_pace: str
    average_heartrate: int | None = None
    max_heartrate: int | None = None
    total_elevation_gain: float | None = None
    strava_url: str | None = None

class Activity(BaseModel):
    external_id: str
    provider: str

    name: str
    sport_type: str

    distance_meters: float
    duration_seconds: int

    average_heart_rate: float | None = None
    max_heart_rate: float | None = None

    elevation_gain_meters: float | None = None