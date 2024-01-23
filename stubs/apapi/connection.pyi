from .alm import ALMConnection as ALMConnection
from .audit import AuditConnection as AuditConnection
from .bulk import BulkConnection as BulkConnection
from .transactional import TransactionalConnection as TransactionalConnection

class Connection(ALMConnection, AuditConnection, BulkConnection, TransactionalConnection): ...
