from sala import Sala
from aluno import Aluno
from professor import Professor

class Controle:

    def __init__(self):
        self.lista_alunos=[]
        self.lista_professores = []
        self.lista_sala = []

    def adicionar_aluno(self,nome,curso, matricula, telefone, email):
        a = Aluno(nome,curso, matricula, telefone, email );
        self.lista_alunos.append(a)

    def adicionar_professor(self,nome,telefone, email):
        p = Professor(nome,telefone,email)
        self.lista_professores.append(p)

    def adicionar_sala(self, denominacao,quantidades_chaves):
        s = Sala(denominacao, quantidades_chaves);
        self.lista_sala.append(s)
        s.imprimir_dados()

    def adicionar_professor_sala(self, professor, nome_sala):
        for i in self.lista_sala:
            if nome_sala == i.denominacao:
                i.adicionar_professor(professor)
                print("\n Professor associado a sala ", nome_sala , " com sucesso")
                i.imprimir_dados()



    def adicionar_aluno_sala(self, aluno, nome_sala):
        for i in self.lista_sala:
            if nome_sala == i.denominacao:
                i.adicionar_aluno(aluno)
                print("\n Aluno associado a sala ", nome_sala, " com sucesso")
                i.imprimir_dados()

    def deletar_aluno(self,nome):

        for i in self.lista_alunos:
            if nome == i.nome:
                self.lista_alunos.remove(i)
                return 0

        return -1 # aluno nao encontrado

    def deletar_professor(self,nome):
        for i in self.lista_professores:
            if nome == i.nome:
                self.lista_professores.remove(i)
                return 0 # tudo ok
        return -1 # professor nao encontrado

    def atualizar_dados_aluno(self, posicao, nome,curso, matricula, telefone, email):
        a = self.lista_alunos[posicao]
        a.nome = nome
        a.curso = curso
        a.matricula = matricula
        a.telefone = telefone
        a.email = email

    def atualizar_dados_professor(self, posicao, nome, telefone,email):
        p = self.lista_professores[posicao]
        p.nome = nome
        p.telefone = telefone
        p.email = email

    def get_aluno(self, posicao):
        a = self.lista_alunos[posicao]
        return a

    def get_aluno_nome(self,nome):

        for i in self.lista_alunos:
            if nome == i.nome:
                return i

    def get_professor(self, posicao):
        p = self.lista_professores[posicao]
        return p

    def get_professor_nome(self, nome):
        for i in self.lista_professores:
            if nome == i.nome:
                return i

    def get_sala(self, posicao):
        s = self.lista_sala[posicao]
        return s

    def get_sala_nome(self, nome_sala):
        for i in self.lista_sala:
            if nome_sala == i.denominacao:
                return i

    def imprimir_dados(self, lista):
        if lista == 0:
            for i in self.lista_alunos:
                print(i.nome)
                print(i.curso)
                print(i.matricula)
                print(i.telefone)
                print(i.email)
        if lista == 1:
            for i in self.lista_professores:
                print(i.nome)
                print(i.telefone)
                print(i.email)

