import unittest
from collections import namedtuple

from musicplayer import __version__
from musicplayer.pytify.auth import AuthMethod
from musicplayer.pytify.core import read_config, Config


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
