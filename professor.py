class Professor:
    def __init__(self, nome , telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def get_nome(self):
        return self.nome

    def imprimir_dados(self):
        print("Nome:", self.nome)
        print("Telefone:", self.telefone)
        print("Email:", self.email)
        return 0
