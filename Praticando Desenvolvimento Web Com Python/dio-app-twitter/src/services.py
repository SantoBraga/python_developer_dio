import tweepy
from src.secrets import *
from src.connection import trends_collection
from src.constants import BRAZIL_WOE_ID


def _get_trends(woe_id: int) -> list[dict[str, any]]:
    """
    Get trending topics.

    :param woe_id: Location identifier.
    :return: Trend topics list.
    """
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = api.get_place_trends(woe_id)

    return trends[0]['trends']


def get_trends_from_mongo() -> list[dict[str, any]]:
    trends = trends_collection.find({})
    return list(trends)


def save_trends() -> None:
    trends = _get_trends(BRAZIL_WOE_ID)
    trends_collection.insert_many(trends)
