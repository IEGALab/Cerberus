from aluno import Aluno

aluno = Aluno("Wellington", "Sistemas", 9456839, "3245-0090", "wel@gmail.com")


def test_criar_aluno():
    assert aluno.email == "wel@gmail.com"

def test_imprimir_dados():
    assert aluno.imprimir_dados() == 0