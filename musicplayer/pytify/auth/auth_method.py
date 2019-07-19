from enum import Enum
from enum import auto


class AuthMethod(Enum):
    CLIENT_CREDENTIALS = auto()
    AUTHORIZATION_CODE = auto()