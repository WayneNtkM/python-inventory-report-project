from inventory_report.inventory.product import Product


string_first = "O produto PS5 fabricado em 12/03/2022 por Sony com validade"
string_second = " até 12/03/3000 precisa ser armazenado Na minha casa."


def test_relatorio_produto():
    product = Product(1, 'PS5', 'Sony', '12/03/2022', '12/03/3000',
                      1234, 'Na minha casa')
    assert product.__repr__() == string_first + string_second
