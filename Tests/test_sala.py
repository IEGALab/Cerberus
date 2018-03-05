from sala import Sala
from aluno import Aluno
from professor import Professor

a1 = Aluno("Wellington", "Sistemas", 9456839, "3245-0090", "wel@gmail.com")
a2 = Aluno("Dani", "Sistemas", 9456839, "3245-0090", "wel@gmail.com")
a3 = Aluno("Thomaz", "Licenciatura em Computação", 9456839, "3245-0090", "wel@gmail.com")

p = Professor("Alex Zissou","3245-6788", "Alex@gmail.com")

alunos = [a1,a2,a3]
professores = [p]

sala = Sala("19", "IEGA", professores,alunos,2)

def test_criar_sala():
    assert sala.quantidade_chaves == 2

def test_imprimir_dados():
    assert sala.imprimir_dados() == 0