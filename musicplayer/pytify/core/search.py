import requests
import json
from urllib.parse import urlencode

from .search_type import SearchType
from musicplayer.pytify.core import read_config


def _search(criteria, auth, search_type):
    """
    Query Spotify for the specified search_type item.

    Args:
        criteria: Represent the search target.
        auth: Authorization information.
        search_type: Search type value.

    Returns:
        Response data in Json format.
    """

    conf = read_config()

    if not criteria:
        raise AttributeError('Parameter `criteria` is required.')

    q_type = search_type.name.lower()
    url = urlencode(f'{conf.base_url}/search?q={criteria}&type={q_type}')

    headers = {'Authorization': f'Bearer {auth.access_token}'}
    response = requests.get(url, headers=headers)

    return json.loads(response.text)


def search_artist(criteria, auth):
    return _search(criteria, auth, SearchType.ARTIST)


def search_album(criteria, auth):
    return _search(criteria, auth, SearchType.ALBUM)


def search_playlist(criteria, auth):
    return _search(criteria, auth, SearchType.PLAYLIST)


def search_track(criteria, auth):
    return _search(criteria, auth, SearchType.TRACK)