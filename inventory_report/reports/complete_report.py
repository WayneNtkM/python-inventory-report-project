from inventory_report.reports.simple_report import SimpleReport
from typing import List, Dict
# from datetime import date, datetime as dt
from collections import Counter


class CompleteReport(SimpleReport):
    simple = SimpleReport()

    @staticmethod
    def generate(param: List[Dict]):
        counter = Counter(x['nome_da_empresa']
                          for x in param)

        company_str = ""

        for k, v in counter.items():
            company_str += f"- {k}: {v}\n"

        return f"""{CompleteReport.simple.generate(param)}
Produtos estocados por empresa:
{company_str}"""
