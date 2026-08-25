from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from app.activity_provider.strava.service import StravaProvider

router = APIRouter(
    prefix = "/providers/strava",
    tags = ["activity providers"],
)


@router.get("/login")
def login():

    provider = StravaProvider()
    authorization_url = provider.build_authorization_url()

    return RedirectResponse(url=authorization_url)


@router.get("/callback")
def callback(
    code: str | None = None, # The variable can contain either a string (`str`) or nothing (`None`).
    scope: str | None = None,
    error: str | None = None,
):
    if error is not None:
        return {
            "status": "authorization_failed",
            "error": error,
        }

    if code is None:
        return {
            "status": "authorization_failed",
            "error": "Authorization code is missing",
        }

    provider = StravaProvider()
    token_data = provider.exchange_authorization_code(code)
    athlete = provider.get_athlete(token_data["access_token"])
    activities = provider.get_activities(
        token_data["access_token"]
    )

    return {
        "status": "connected",
        "athlete_id": athlete["id"],
        "firstname": athlete.get("firstname"),
        "lastname": athlete.get("lastname"),
        "activities_count": len(activities),
        "activities": activities,
    }