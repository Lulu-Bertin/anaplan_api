from .authentication import AbstractAuth as AbstractAuth
from .utils import API_URL as API_URL
from _typeshed import Incomplete
from requests import Response

class BasicConnection:
    details: bool
    compress: bool
    timeout: float
    authentication: Incomplete
    def __init__(self, authentication: AbstractAuth, api_url: str = ...) -> None: ...
    def request(self, method: str, url: str, params: dict = None, data: Incomplete | None = None, headers: Incomplete | None = None) -> Response: ...
