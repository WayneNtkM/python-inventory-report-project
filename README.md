
# Inventory-Report

Projeto realizado durante o curso da Trybe. Consiste em leitura de arquivos csv, json e xml utilizando python. Cada arquivo é aberto, lido e apresentado em forma de dicionários para o usuário.


## Tecnologias utilizadas

Python, xmltodict, pytest, flake8, black


## Rodando localmente

Clone o projeto

```bash
  git clone git@github.com:WayneNtkM/python-inventory-report-project.git
```

Entre no diretório do projeto

```bash
  cd my-project
```

Crie o ambiente virtual

```bash
   python3 -m venv .venv && source .venv/bin/activate
```

Instale as dependências

```bash
  python3 -m pip install -r dev-requirements.txt
```


## Rodando os testes

Para rodar os testes, rode um dos seguintes comandos:

Todos os testes:
```bash
$ python3 -m pytest
```

Caso precise executar apenas um arquivo de testes basta executar o comando:

```bash
python3 -m pytest tests/nomedoarquivo.py
```

Caso precise executar apenas uma função de testes basta executar o comando:

```bash
python3 -m pytest -k nome_da_func_de_tests
```

Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro -x
```bash
python3 -m pytest -x tests/test_simple_report.py
```

Caso queria executar um teste especifico de um arquivo basta executar o comando:
```bash
python3 -m pytest -x tests/nomedoarquivo.py::test_nome_do_teste
```


## Docker

Caso queria executar os seus testes de projeto via `Docker-compose`, substituindo o ambiente virtual, execute o comando:
```bash
    docker-compose run --rm inventory pytest
```
