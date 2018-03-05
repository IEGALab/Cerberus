from registro import Registro
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
r = Registro(sala, "Wellington")
r2 = Registro(sala,"Dani")
r3 = Registro(sala,"Thomaz")
sala2 = Sala("23","Acessar",p,[],1) # lista de alunos vazia, sala sem aluno


def test_emprestar_ok():
    assert r.pegar_chave()==0


def test_devolver_ok():
    assert r.devolver_chave()==0


def test_emprestar_aluno_notOk():
    r = Registro(sala, "Junior")
    assert r.pegar_chave() == -1


def test_sem_chave():
    #print("chaves:",sala.quantidade_chaves)
    r.pegar_chave()
    r2.pegar_chave()
    assert r3.pegar_chave()== -2


def test_sala_sem_aluno():
    r = Registro(sala2,"Junior")
    assert r.pegar_chave()== -1

def test_imprimir_dados():
    print("Chaves:", sala.quantidade_chaves)
    assert r.imprimir_dados()==0
    assert r2.imprimir_dados()==0
    assert r3.imprimir_dados()==0