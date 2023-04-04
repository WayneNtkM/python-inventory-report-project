import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, t: str):
        with open(path, 'r') as file:
            file_converted = str

            if path.endswith('.csv'):
                file_converted = list(csv.DictReader(file))
            elif path.endswith('.json'):
                file_converted = json.load(file)
            else:
                file_converted = xmltodict.parse(
                    file.read())['dataset']['record']

            if t == 'simples':
                return SimpleReport.generate(file_converted)
            else:
                return CompleteReport.generate(file_converted)
