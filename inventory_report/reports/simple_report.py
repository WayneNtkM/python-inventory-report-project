from typing import List, Dict
from datetime import date, datetime as dt
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(param: List[Dict]) -> str:
        min_date = min(d['data_de_fabricacao'] for d in param)
        expiration_date = min(d['data_de_validade'] for d in param
                              if dt.strptime(d['data_de_validade'], "%Y-%m-%d")
                              .date()
                              > date.today())
        [(company, _)] = Counter(x['nome_da_empresa']
                                 for x in param).most_common(1)

        return f"""Data de fabricação mais antiga: {min_date}
Data de validade mais próxima: {expiration_date}
Empresa com mais produtos: {company}"""
