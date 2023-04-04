from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(path: str, t: str):
        if path.endswith('.csv'):
            file_converted = CsvImporter().import_data(path)
        elif path.endswith('.json'):
            file_converted = JsonImporter().import_data(path)
        else:
            file_converted = XmlImporter().import_data(path)

        if t == 'simples':
            return SimpleReport.generate(file_converted)
        else:
            return CompleteReport.generate(file_converted)
