from inventory_report.reports.simple_report import SimpleReport
from typing import List, Dict
from datetime import date, datetime as dt
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(param: List[Dict]):
        min_date = min(d['data_de_fabricacao'] for d in param)
        expiration_date = min(d['data_de_validade'] for d in param
                              if dt.strptime(d['data_de_validade'], "%Y-%m-%d")
                              .date()
                              > date.today())
        counter = Counter(x['nome_da_empresa']
                          for x in param)

        [(company, _)] = counter.most_common(1)

        company_str = ""

        for k, v in counter.items():
            company_str += f"- {k}: {v}\n"

        return f"""Data de fabricação mais antiga: {min_date}
Data de validade mais próxima: {expiration_date}
Empresa com mais produtos: {company}
Produtos estocados por empresa:
{company_str}"""
