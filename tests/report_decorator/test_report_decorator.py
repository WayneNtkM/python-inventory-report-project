from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import sys


products_list = [
    {
        "id": 1,
        "nome_do_produto": "Cafe",
        "nome_da_empresa": "Cafes Nature",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-12-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "instrucao"
    },
    {
        "id": 2,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2022-04-04",
        "data_de_validade": "2023-12-12",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco"
    }
]


def test_decorar_relatorio(capsys):
    sys.stdout.write(ColoredReport(SimpleReport).generate(products_list))

    test, _ = capsys.readouterr()

    assert test == 'OLSKDKS'
