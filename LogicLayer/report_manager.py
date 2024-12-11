from StorageLayer import StorageAPI

from Model import Report

class ReportManager:
    def __init__(self, storage_api : StorageAPI):
        self.storage_api = storage_api

    def report_get_all(self) -> list[Report]:
        return self.storage_api.report_get_all()

    def report_get_by_ID(self, reportID : str) -> Report:
        return self.storage_api.report_get_by_ID(reportID)

    def report_add(self, new_report : Report) -> None:
        self.storage_api.report_add(new_report)

    def report_edit(self, edited_report : Report) -> None:
        self.storage_api.report_edit(edited_report)

    def report_remove(self, reportID : str) -> None:
        self.storage_api.report_remove(reportID)

    def report_search(self, search_string : str) -> list[Report]:
        # TODO
        return []
