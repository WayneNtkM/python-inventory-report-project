from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if path.endswith('.csv'):
            with open(path, 'r') as file:
                return list(csv.DictReader(file))
        else:
            raise ValueError('Arquivo inválido')
