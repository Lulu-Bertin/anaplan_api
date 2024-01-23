from .authentication import AbstractAuth as AbstractAuth
from .basic_connection import BasicConnection as BasicConnection
from .utils import API_URL as API_URL, AUDIT_URL as AUDIT_URL, AuditEventType as AuditEventType, MIMEType as MIMEType, PAGING_LIMIT as PAGING_LIMIT
from requests import Response

class AuditConnection(BasicConnection):
    def __init__(self, authentication: AbstractAuth, api_url: str = ..., _audit_url: str = ...) -> None: ...
    def get_events(self, event_type: AuditEventType = ..., accept: MIMEType = ..., date_from: int = None, date_to: int = None, interval: int = None) -> Response: ...
    def search_events(self, event_type: AuditEventType = ..., accept: MIMEType = ..., date_from: int = None, date_to: int = None, interval: int = None) -> Response: ...