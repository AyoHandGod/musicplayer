from .parameter import prepare_params
from .execute_request import execute_request


def get_album_tracks(album_id, auth, params=None):
    """
    Retrieve the tracks from specfied album_id.

    Args:
        album_id: Id number of target album.
        auth: Spotify authentication.
        params: Search parameters.

    Returns:
        Album tracklist in JSON format.

    """

    if album_id is None or album_id is "":
        raise AttributeError('Parameter `album_id` cannot be `None` or empty.')

    url_template = '{base_url}/{area}/{albumid}/{postfix}{query}'
    url_params = {
        'query': prepare_params(params),
        'area': 'albums',
        'albumid': album_id,
        'postfix': 'tracks',
    }

    return execute_request(url_template, auth, url_params)
