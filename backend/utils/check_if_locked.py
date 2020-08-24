import json
from datetime import datetime, timedelta

from backend.utils.get_path_utils import get_lock_data_file_path


def check_if_locked(token: str, secs_thr: int = 5) -> bool:
    with open(get_lock_data_file_path()) as data_file:
        json_data = json.load(data_file)

    # If last connection is None then it is the first time anybody connects thus database is not blocked.
    if json_data['last_connection'] is None:
        return False

    # Otherwise we must check if its been enough time since last connection. If so then database is not blocked.
    now = datetime.now()
    last_connection = datetime.fromisoformat(json_data['last_connection'])
    if now - last_connection > timedelta(seconds=secs_thr):
        return False

    # If not enough time has passed since last connection then database is blocked.
    # However we must check if it blocked by the same user with the given token.
    # Is so the database is not blocked for that user.
    if token == json_data['token']:
        return False
    else:
        # Database has been accessed by someone else very little time from now. you cannot access it now.
        return True
