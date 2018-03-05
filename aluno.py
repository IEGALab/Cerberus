
class Aluno:

    def __init__(self,nome,curso, matricula, telefone, email ):
        self.nome = nome
        self.curso = curso
        self.matricula= matricula
        self.telefone = telefone
        self.email = email

    def get_nome(self):
        return self.nome

    def imprimir_dados(self):
        print("Nome:", self.nome)
        print("Curso:", self.curso)
        print("Matricula:", self.matricula)
        print("Telefone:", self.telefone)
        print("Email:", self.email)
        return 0
