import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from apapi.utils import AUTH_URL as AUTH_URL, OAUTH2_URL as OAUTH2_URL, get_generic_session as get_generic_session
from enum import Enum
from requests import Session
from requests.auth import AuthBase
from typing import Callable

class AnaplanAuth(AuthBase):
    token: Incomplete
    def __init__(self, token) -> None: ...
    def __call__(self, r): ...

class AuthType(Enum):
    BASIC: str
    CERT: str
    OAUTH2_NONROTATABLE: str
    OAUTH2_ROTATABLE: str

class AbstractAuth(ABC, metaclass=abc.ABCMeta):
    session: Incomplete
    def __init__(self, auth_url: str = ..., session: Session = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    @property
    @abstractmethod
    def auth_type(self) -> AuthType: ...
    @abstractmethod
    def authenticate(self) -> None: ...
    def refresh_token(self) -> None: ...
    def validate_token(self) -> bool: ...
    def close(self) -> None: ...

class BasicAuth(AbstractAuth):
    def __init__(self, credentials: str, auth_url: str = ..., session: Session = ...) -> None: ...
    @property
    def auth_type(self) -> AuthType: ...
    def authenticate(self) -> None: ...

class OAuth2NonRotatable(AbstractAuth):
    def __init__(self, client_id: str, refresh_token: str, oauth2_url: str = ..., auth_url: str = ..., session: Session = ...) -> None: ...
    @property
    def auth_type(self) -> AuthType: ...
    def authenticate(self) -> None: ...

class OAuth2Rotatable(AbstractAuth):
    def __init__(self, client_id: str, refresh_token_getter: Callable[[], str], refresh_token_setter: Callable[[str], None], oauth2_url: str = ..., auth_url: str = ..., session: Session = ...) -> None: ...
    @property
    def auth_type(self) -> AuthType: ...
    def authenticate(self) -> None: ...
