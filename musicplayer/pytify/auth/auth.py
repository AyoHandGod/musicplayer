import requests
import os
import base64
import json

from musicplayer.pytify.auth import AuthMethod
from musicplayer.pytify.core.config import Config
from .authorization import Authorization
from ..core import BadRequestError


def get_auth_key(client_id: str, client_secret: str):
    """
    Encode/decode client_id and client_secret to base64 string.

    Args:
        client_id (str): Client ID as string.
        client_secret (str): Client secret key as string.

    Returns:
        Base64 decoded string of client_id and client_secret
    """
    byte_keys = bytes(f'{client_id}:{client_secret}', 'utf-8')
    encoded_key = base64.b64encode(byte_keys)
    return encoded_key.decode('utf-8')


def _authorization_code(conf):
    current_dir = os.path.abspath(os.curdir)
    file_path = os.path.join(current_dir, '.pytify')

    auth_key = get_auth_key(conf.client_id, conf.client_secret)

    try:
        with open(file_path, mode='r', encoding='UTF-8') as file:
            refresh_token = file.readline()

            if refresh_token:
                return _refresh_access_token(auth_key, refresh_token)

    except IOError:
        raise IOError(('It seems you have not authorized the application yet '
                       '. The file .pytify was not found.'))


def _client_credentials(conf: Config):
    """
    Parse config and send request to Spotify in order to create
    Authorization.

    Args:
        conf: Config object.

    Returns:
        Authorization object if successful, else raises BadRequestError.
    """
    auth_key = get_auth_key(conf.client_id, conf.client_secret)

    headers = {'Authorization': f'Basic {auth_key}', }

    options = {
        'grant_type': 'client_credentials',
        'json': True,
    }

    response = requests.post('https://accounts.spotify.com/api/token',
                             headers=headers,
                             data=options)

    content = json.loads(response.content.decode('utf-8'))

    if response.status_code == 400:
        error_description = content.get('error_description', '')
        raise BadRequestError(error_description)

    access_token = content.get('access_token', None)
    token_type = content.get('token_type', None)
    expires_in = content.get('expires_in', None)
    scope = content.get('scope', None)

    return Authorization(access_token, token_type, expires_in, scope, None)


def _refresh_access_token(auth_key, refresh_token):
    """
    Refresh Authorization object for request.

    Args:
        auth_key:
        refresh_token:

    Returns:

    """
    headers = {'Authorization': f'Basic{auth_key}', }

    options = {
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token',
    }

    response = requests.post(
        'https://accounts/spotify.com/api/token',
        headers=headers,
        data=options
    )

    content = json.loads(response.content.decode('utf-8'))

    if not response.ok:
        error_description = content.get('error_description', None)
        raise BadRequestError(error_description)

    access_token = content.get('access_token', None)
    token_type = content.get('token_type', None)
    scope = content.get('scope', None)
    expires_in = content.get('expires_in', None)

    return Authorization(access_token, token_type, expires_in, scope, None)


def authenticate(conf: Config):
    """
    Use Config object to obtain access_token.

    Args:
        conf: Config object.

    Returns:
        access_token.
    """
    if conf.auth_method == AuthMethod.CLIENT_CREDENTIALS:
        return _client_credentials(conf)

    return _authorization_code(conf)
