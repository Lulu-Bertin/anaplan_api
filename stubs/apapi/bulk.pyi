from .basic_connection import BasicConnection as BasicConnection
from .utils import DEFAULT_DATA as DEFAULT_DATA, MIMEType as MIMEType
from requests import Response

class BulkConnection(BasicConnection):
    def generic_get_actions(self, model_id: str, action_type: str) -> Response: ...
    def get_imports(self, model_id: str) -> Response: ...
    def get_exports(self, model_id: str) -> Response: ...
    def get_actions(self, model_id: str) -> Response: ...
    def get_processes(self, model_id: str) -> Response: ...
    def get_files(self, model_id: str) -> Response: ...
    def get_import(self, model_id: str, import_id: str) -> Response: ...
    def get_export(self, model_id: str, export_id: str) -> Response: ...
    def get_process(self, model_id: str, process_id: str, details: bool = None) -> Response: ...
    def put_file(self, model_id: str, file_id: str, data: bytes) -> Response: ...
    def upload_file(self, model_id: str, file_id: str, data: [bytes], content_type: MIMEType = ...) -> Response: ...
    def get_file(self, model_id: str, file_id: str) -> Response: ...
    def download_file(self, model_id: str, file_id: str) -> [bytes]: ...
    def delete_file(self, model_id: str, file_id: str) -> Response: ...
    def generic_run_action(self, model_id: str, action_id: str, action_type: str, data: dict = None) -> Response: ...
    def run_import(self, model_id: str, import_id: str, data: dict = None) -> Response: ...
    def run_export(self, model_id: str, export_id: str) -> Response: ...
    def run_action(self, model_id: str, action_id: str) -> Response: ...
    def run_process(self, model_id: str, process_id: str, data: dict = None) -> Response: ...
    def generic_get_action_tasks(self, model_id: str, action_id: str, action_type: str) -> Response: ...
    def get_import_tasks(self, model_id: str, import_id: str) -> Response: ...
    def get_export_tasks(self, model_id: str, export_id: str) -> Response: ...
    def get_action_tasks(self, model_id: str, action_id: str) -> Response: ...
    def get_process_tasks(self, model_id: str, process_id: str) -> Response: ...
    def generic_get_action_task(self, model_id: str, action_id: str, task_id: str, action_type: str) -> Response: ...
    def get_import_task(self, model_id: str, import_id: str, task_id: str) -> Response: ...
    def get_export_task(self, model_id: str, export_id: str, task_id: str) -> Response: ...
    def get_action_task(self, model_id: str, action_id: str, task_id: str) -> Response: ...
    def get_process_task(self, model_id: str, process_id: str, task_id: str) -> Response: ...
    def get_import_dump(self, model_id: str, import_id: str, task_id: str) -> Response: ...
    def download_import_dump(self, model_id: str, import_id: str, task_id: str) -> bytes: ...
    def get_process_dump(self, model_id: str, process_id: str, task_id: str, object_id: str) -> Response: ...
    def download_process_dump(self, model_id: str, process_id: str, task_id: str, object_id: str) -> bytes: ...