from StorageLayer.base_storage import BaseStorage

from Model import Report

class ReportStorage(BaseStorage):
    def __init__(self, filename, model_class) -> None:
        super().__init__(filename, model_class)

    def report_add(self, new_report : Report) -> None:
        current_reports : list[Report] = self.load_from_file()
        current_reports.append(new_report)
        self.save_to_file(current_reports)

    def report_remove(self, reportID: str):
        current_reports : list[Report] = self.load_from_file()

        new_reports_list = []
        for report in current_reports:
            if report.reportID != reportID:
                new_reports_list.append(report)

        self.save_to_file(new_reports_list)

    def report_edit(self, edited_report : Report):
        current_reports : list[Report] = self.load_from_file()

        new_reports_list = []
        for report in current_reports:
            if report.reportID == edited_report.reportID:
                new_reports_list.append(edited_report)
            else:
                new_reports_list.append(report)

        self.save_to_file(new_reports_list)

    def report_get_all(self) -> list[Report]:
        return self.load_from_file()

    def report_get_by_ID(self, reportID : str) -> Report:
        current_reports : list[Report] = self.load_from_file()
        for report in current_reports:
            if report.reportID == reportID:
                return report

    def report_search(self, search_string : str) -> list[Report]:
        return []
