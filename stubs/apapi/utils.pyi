from .__version__ import __version__ as __version__
from enum import Enum
from requests import Session
from typing import Final

class ExportType(Enum):
    GRID: str
    TABULAR_SINGLE: str
    TABULAR_MULTI: str

class MIMEType(Enum):
    APP_JSON: str
    APP_8STREAM: str
    APP_GZIP: str
    TEXT_CSV: str
    TEXT_CSV_ESCAPED: str
    TEXT_PLAIN: str

class ModelOnlineStatus(Enum):
    OFFLINE: str
    ONLINE: str

class AuditEventType(Enum):
    ALL: str
    BYOK: str
    USER_ACTIVITY: str

API_URL: Final[str]
AUDIT_URL: Final[str]
AUTH_URL: Final[str]
OAUTH2_URL: Final[str]
USER_AGENT: Final[str]
DEFAULT_HEADERS: Final[dict]
DEFAULT_DATA: Final[dict]
ENCODING_GZIP: Final[str]
PAGING_LIMIT: Final[int]

def get_generic_session(retry_count: int = 3) -> Session: ...
def start_oauth2_flow(client_id: str, oauth2_url: str = ..., session: Session = ...) -> dict: ...
def obtain_oauth2_token(client_id: str, device_code: str, oauth2_url: str = ..., session: Session = ...) -> dict: ...
