import unittest
from collections import namedtuple

from musicplayer import __version__
from musicplayer.pytify.auth import AuthMethod, Authorization
from musicplayer.pytify.core import read_config
from musicplayer.pytify.core.config import Config


def test_version():
    assert __version__ == '0.1.0'


class ConfigurationTest(unittest.TestCase):

    def test_can_load_auth_method(self):
        client = AuthMethod.CLIENT_CREDENTIALS
        auth_code = AuthMethod.AUTHORIZATION_CODE
        self.assertIs(type(client and auth_code), AuthMethod, "Client and auth not AuthMethods.")

    def test_can_load_config_file(self):
        config = read_config()
        self.assertIs(type(config), Config, "Config is not a namedtuple")

    def test_can_retrieve_client_id_from_config(self):
        config = read_config()
        client_id = config.client_id
        self.assertEqual(client_id, 'test_id', 'Client ID does not match ' + client_id)

    def test_can_retrieve_client_secret_from_config(self):
        self.assertEqual(read_config().client_secret, 'secret_id', 'Secret id does not match. ' + read_config()
                         .client_secret)

    def test_can_retrieve_access_token_url_from_config(self):
        self.assertEqual(read_config().access_token_url, 'https://accounts.spotify.com/api/token',
                         'Access token URL did'
                         'not match.')

    def test_can_retrieve_auth_url_from_config(self):
        self.assertEqual(read_config().auth_url, 'http://accounts.spotify.com/authorize', "Authorization URL did not "
                                                                                          "match.")

    def test_can_retrieve_api_version_from_config(self):
        self.assertEqual(read_config().api_version, 'v1', 'API version did not match.')

    def test_can_retrieve_api_url_from_config(self):
        self.assertEqual(read_config().api_url, 'https://api.spotify.com', 'API URL did not match.')

    def test_can_retrieve_auth_method_from_config(self):
        self.assertEqual(read_config().auth_method, 'AUTHORIZATION_CODE', 'Auth code mismatch.')


class AuthorizationTest(unittest.TestCase):

    def test_authorization_model_exists(self):
        auth = Authorization(access_token='test', token_type='test_token', expires_in='100',
                             scope='test_scope', refresh_token='refresh_test')
        self.assertIs(type(auth), Authorization(), "Type is not Authorization.")


class BadRequestErrorTest(unittest.TestCase):
    pass
