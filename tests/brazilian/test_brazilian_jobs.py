import pytest
from src.pre_built.brazilian_jobs import read_brazilian_file


@pytest.fixture
def return_of_list_of_dict():
    return [
        {"salary": "2000", "title": "Maquinista", "type": "trainee"},
        {"salary": "3000", "title": "Motorista", "type": "full time"},
        {
            "salary": "4000",
            "title": "Analista de Software",
            "type": "full time",
        },
        {
            "salary": "1700",
            "title": "Assistente administrativo",
            "type": " full time",
        },
        {
            "salary": "1400",
            "title": "Auxiliar administrativo",
            "type": " full time",
        },
        {"salary": "1400", "title": "Auxiliar usinagem", "type": " full time"},
        {
            "salary": "1400",
            "title": "Auxiliar de padaria",
            "type": " full time",
        },
        {"salary": "1400", "title": "Analista Contábil", "type": " full time"},
        {"salary": "5000", "title": "Gerente comercial", "type": " full time"},
        {
            "salary": "4000",
            "title": "Analista de Departamento Pessoal",
            "type": " full time",
        },
        {
            "salary": "50000",
            "title": "Esportista de Futebol profissional",
            "type": " full time",
        },
        {
            "salary": "4000",
            "title": "Analista de crédito",
            "type": " full time",
        },
        {
            "salary": "3000",
            "title": "Pessoa Programadora",
            "type": " full time",
        },
        {"salary": "3000", "title": "Ux Designer", "type": " full time"},
        {
            "salary": " 1400",
            "title": "Auxiliar de manutenção",
            "type": " full time",
        },
    ]


@pytest.fixture
def bad_return_of_list_of_dict():
    return [
        {"salario": "2000", "title": "Maquinista", "type": "trainee"},
        {"salario": "3000", "title": "Motorista", "type": "full time"},
        {
            "salario": "4000",
            "title": "Analista de Software",
            "type": "full time",
        },
        {
            "salario": "1700",
            "title": "Assistente administrativo",
            "type": " full time",
        },
        {
            "salario": "1400",
            "title": "Auxiliar administrativo",
            "type": " full time",
        },
        {
            "salario": "1400",
            "title": "Auxiliar usinagem",
            "type": " full time",
        },
        {
            "salario": "1400",
            "title": "Auxiliar de padaria",
            "type": " full time",
        },
        {
            "salario": "1400",
            "title": "Analista Contábil",
            "type": " full time",
        },
        {
            "salario": "5000",
            "title": "Gerente comercial",
            "type": " full time",
        },
        {
            "salario": "4000",
            "title": "Analista de Departamento Pessoal",
            "type": " full time",
        },
        {
            "salario": "50000",
            "title": "Esportista de Futebol profissional",
            "type": " full time",
        },
        {
            "salario": "4000",
            "title": "Analista de crédito",
            "type": " full time",
        },
        {
            "salario": "3000",
            "title": "Pessoa Programadora",
            "type": " full time",
        },
        {"salario": "3000", "title": "Ux Designer", "type": " full time"},
        {
            "salario": " 1400",
            "title": "Auxiliar de manutenção",
            "type": " full time",
        },
    ]


def test_brazilian_jobs(return_of_list_of_dict, bad_return_of_list_of_dict):
    assert (
        read_brazilian_file("tests/mocks/brazilians_jobs.csv")
        == return_of_list_of_dict
    )
    assert (
        read_brazilian_file("tests/mocks/brazilians_jobs.csv")
        != bad_return_of_list_of_dict
    )
