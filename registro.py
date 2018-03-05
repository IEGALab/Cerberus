"""
Quando tiver a interface grafica vou criar o registro, verificar se tem chaves
disponiveis, se tiver, ok registra, caso contrario não registra e apaga a referencia

"""


class Registro:

    def __init__(self, sala, nome_aluno):
        self.sala = sala
        self.nome_aluno = nome_aluno
        self.status = "sem chave disponivel"
        #TODO:  pegar data e hora aqui

    def pegar_chave(self):

        # testar primeiro se sala ainda tem alguma chave para emprestar
        if self.sala.quantidade_chaves > 0:
            # testar se aluno esta cadastrado a pegar a chave
            flag = 0
            for i in self.sala.alunos:
                if i.nome == self.nome_aluno:
                    self.sala.quantidade_chaves -= 1
                    self.status ="Chave emprestada"
                    flag = 1
                    break
            if flag == 1: # tem chave disponivel e aluno esta autorizado
                return 0  # ok em alocar sala
            else:
                return -1 # tem chave disponivel mas aluno não esta na lista de autorizados
        else:
            return -2 # sem chave para emprestar


    def devolver_chave(self):
        #TODO  procurar no registro de emprestimos se a chave estava emprestada mesmo astes de devolver

        print("Aluno", self.nome_aluno, " devolveu a chave da sala:", self.sala.id, "-", self.sala.denominacao)
        self.status = "Chave Devolvida"
        self.sala.quantidade_chaves +=1
        return 0

    #verificar se o aluno esta cadastrado para pegar chave antes de emprestar
    # desnecessario se aluno vier dos alunos cadastrados em cada sala ...
    def imprimir_dados(self):
        print("Aluno:",self.nome_aluno)
        print(self.sala.id,"-", self.sala.denominacao)
        print("Status:", self.status)
        return 0
