from professor import Professor

professor = Professor("Alex Zissou","3245-6788", "Alex@gmail.com")

def test_criar_professor():
    assert professor.nome == "Alex Zissou"

def test_imprimir_dados():
    assert professor.imprimir_dados()==0