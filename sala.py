class Sala:

    def __init__(self,  denominacao, quantidade_chaves):
        self.denominacao = denominacao
        self.professores = []
        self.alunos = []
        self.quantidade_chaves = quantidade_chaves

    def adicionar_professor(self, professor):
        self.professores.append(professor)


    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def get_lista_professores(self):
        return self.professores

    def get_lista_alunos(self):
        return self.alunos


    def imprimir_dados(self):
        print("Sala -", self.denominacao)
        print("Professores Responsaveis:")
        if len(self.professores) == 0 :
            print("Nenhum professor associado")
        else:
            for i in self.professores:
                print(i.nome)

        print("Alunos associados a Sala:")
        if len(self.alunos)==0:
            print("Nenhum aluno associado a sala")
        else:
            for i in self.alunos:
                print(i.imprimir_dados())
        print("Numero de chaves :", self.quantidade_chaves)
        return 0