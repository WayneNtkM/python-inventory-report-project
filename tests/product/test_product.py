from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(1, 'Faca Tramontina', 'Tramontina', '12/03/1999',
                      'sem validade', 1324, 'Cuidar para não se cortar')
    assert product.id == 1
    assert product.data_de_validade == 'sem validade'
    assert product.nome_da_empresa == 'Tramontina'
    assert product.nome_do_produto == 'Faca Tramontina'
    assert product.data_de_fabricacao == '12/03/1999'
    assert product.numero_de_serie == 1324
    assert product.instrucoes_de_armazenamento == 'Cuidar para não se cortar'
