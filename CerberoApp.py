from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from UI import MainWindow
from UI import DialogAluno
from UI import DialogProf

import sys
from controle import Controle
from datetime import datetime

__appname__ = "Cerberus"


class Form(QMainWindow, MainWindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(__appname__)
        self.dados = Controle()

        self.tableWidgetRegistros.setColumnWidth(1, 200)
        # Todos os eventos da interface grafica
        self.pushButtonAdicionarAluno.clicked.connect(self.adicionar_aluno)
        self.pushButtonRemoverAluno.clicked.connect(self.apagar_aluno)
        self.pushButtonEditarAluno.clicked.connect(self.editar_dados_aluno)
        self.pushButtonVerDados.clicked.connect(self.ver_dados_aluno)
        self.pushButtonProfAdicionar.clicked.connect(self.adicionar_professor)
        self.pushButtonProfRemover.clicked.connect(self.apagar_professor)
        self.pushButtonProfEditar.clicked.connect(self.editar_dados_professor)
        self.pushButtonProfVerDados.clicked.connect(self.ver_dados_professor)
        self.pushButtonAdicionarSala.clicked.connect(self.adicionar_sala)
        self.pushButtonAddProfSala.clicked.connect(self.associar_professor_sala)
        self.pushButtonAddAlunoSala.clicked.connect(self.associar_aluno_sala)
        self.listWidgetSalasCadastradas.itemClicked.connect(self.atualizar_dados_sala)
        self.comboBoxSalasRegistro.currentIndexChanged.connect(self.povoar_combobox_alunoRegistro)
        self.pushButton_Emprestar.clicked.connect(self.emprestar_chave)
        self.pushButton_Devolver.clicked.connect(self.devolver_chave)

    """
    Aqui ficam todos os metodos necessarios da aba alunos
    
    """


    def adicionar_aluno(self):
        nome = self.lineEditAlunoNome.text()
        curso = self.comboBoxCurso.currentText()
        matricula = self.lineEditMatricula.text()
        telefone = self.lineEditTelefone.text()
        email = self.lineEditEmail.text()
        self.dados.adicionar_aluno(nome,curso,matricula,telefone,email)
        self.listWidgetAlunos.addItem(nome)# na secao aluno
        self.listWidgetSalaAluno.addItem(nome) # na secao sala
        self.limpar_campos()

    def apagar_aluno(self):
        linha_selecionada = self.listWidgetAlunos.currentRow()
        if linha_selecionada == -1:
            msg = QMessageBox()
            msg.setText("Nenhum aluno selecionado!")
            msg.exec_()
        else:
            item = self.listWidgetAlunos.takeItem(linha_selecionada)  # secao aluno
            self.listWidgetSalaAluno.takeItem(linha_selecionada)  # secao sala
            nome = item.text()
            self.dados.deletar_aluno(nome)


    def ver_dados_aluno(self):
        linha_selecionada = self.listWidgetAlunos.currentRow()
        aluno = self.dados.get_aluno(linha_selecionada)
        self.lineEditAlunoNome.setText(aluno.nome)
        curso = aluno.curso
        indice = self.comboBoxCurso.findText(curso)
        self.comboBoxCurso.setCurrentIndex(indice)
        self.lineEditMatricula.setText(aluno.matricula)
        self.lineEditTelefone.setText(aluno.telefone)
        self.lineEditEmail.setText(aluno.email)


    def ver_dados_professor(self):
        linha_selecionada = self.listWidgetProf.currentRow()
        p = self.dados.get_professor(linha_selecionada)
        self.lineEditProfNome.setText(p.nome)
        self.lineEditProfTelefone.setText(p.telefone)
        self.lineEditProfEmail.setText(p.email)


    def editar_dados_aluno(self):
        linha_selecionada = self.listWidgetAlunos.currentRow()
        if linha_selecionada == -1:
            msg = QMessageBox()
            msg.setText("Nenhum aluno selecionado!")
            msg.exec_()
        else:
            aluno = self.dados.get_aluno(linha_selecionada)
            d = AlunoDialog()
            d.lineNome.setText(aluno.nome)
            curso = aluno.curso
            indice = self.comboBoxCurso.findText(curso)
            d.comboBoxCurso.setCurrentIndex(indice)
            d.lineMatricula.setText(aluno.matricula)
            d.lineTelefone.setText(aluno.telefone)
            d.lineEmail.setText(aluno.email)
            if d.exec_():
                nome = d.lineNome.text()
                curso = d.comboBoxCurso.currentText()
                matricula = d.lineMatricula.text()
                telefone = d.lineTelefone.text()
                email = d.lineEmail.text()
                self.dados.atualizar_dados_aluno(linha_selecionada, nome, curso, matricula, telefone, email)
                self.listWidgetAlunos.takeItem(linha_selecionada)
                self.listWidgetAlunos.insertItem(linha_selecionada, nome)
                self.listWidgetSalaAluno.takeItem(linha_selecionada)
                self.listWidgetSalaAluno.insertItem(linha_selecionada, nome)


    """
    Aqui ficam todos os metodos necessarios da aba professores
    
    """


    def adicionar_professor(self):
        # adiciona o professor a lista de cadastrados na aba professor
        nome = self.lineEditProfNome.text()
        telefone = self.lineEditProfTelefone.text()
        email = self.lineEditProfEmail.text()
        self.dados.adicionar_professor(nome,telefone,email)
        self.listWidgetProf.addItem(nome)
        self.listWidgetSalaProf.addItem(nome)
        self.limpar_campos()
        self.dados.imprimir_dados(1)

    def apagar_professor(self):
        linha_selecionada = self.listWidgetProf.currentRow()
        if linha_selecionada == -1:
            msg = QMessageBox()
            msg.setText("Nenhum professor selecionado!")
            msg.exec_()
        else:
            item = self.listWidgetProf.takeItem(linha_selecionada)  # secao aluno
            self.listWidgetSalaProf.takeItem(linha_selecionada)  # secao sala
            nome = item.text()
            self.dados.deletar_professor(nome)


    def editar_dados_professor(self):
        linha_selecionada = self.listWidgetProf.currentRow()
        if linha_selecionada == -1:
            msg = QMessageBox()
            msg.setText("Nenhum professor selecionado!")
            msg.exec_()
        else:
            professor = self.dados.get_professor(linha_selecionada)
            d = ProfDialog()
            d.lineEditProfNome.setText(professor.nome)
            d.lineEditProfTelefone.setText(professor.telefone)
            d.lineEditProfEmail.setText(professor.email)
            if d.exec_():
                nome = d.lineEditProfNome.text()
                telefone = d.lineEditProfTelefone.text()
                email = d.lineEditProfEmail.text()
                self.dados.atualizar_dados_professor(linha_selecionada, nome, telefone, email)
                self.listWidgetProf.takeItem(linha_selecionada)
                self.listWidgetProf.insertItem(linha_selecionada, nome)
                self.listWidgetSalaProf.takeItem(linha_selecionada)
                self.listWidgetSalaProf.insertItem(linha_selecionada, nome)


    """
    Aqui ficam todos os metodos necessarios da aba salas
    
    """



    def adicionar_sala(self):
        # adiciona a sala em uma lista de salas na aba sala

        nome_sala =  self.lineEditIdSala.text()
        quantidades_chaves = self.spinBoxNumeroChaves.text()

        # cadastra sala na lista
        self.listWidgetSalasCadastradas.addItem(nome_sala)
        self.dados.adicionar_sala(nome_sala,quantidades_chaves)
        # Limpar campos
        self.lineEditIdSala.clear()
        self.spinBoxNumeroChaves.setValue(0)

        #povoar a combobox de sala na aba de registro
        self.comboBoxSalasRegistro.addItem(nome_sala)


        # TODO : implementar a rotida de editar os valores da sala em uma nova versao
        # editando os valores da sala em um form em separado como se edita o professor ou aluno


    def associar_professor_sala(self):

        #testar se tem professor selecionado na lista
        linha_selecionada = self.listWidgetSalaProf.currentRow()

        if linha_selecionada == -1:
            msg = QMessageBox()
            msg.setText("Nenhum professor selecionado!")
            msg.exec_()
            return -1 # retornar -1 significa que nao tem professor selecionado

        # testar se tem sala selecionada na lista
        sala_selecionada = self.listWidgetSalasCadastradas.currentRow()

        if sala_selecionada == -1:
            msg = QMessageBox()
            msg.setText("Nenhuma sala cadastrada foi selecionada!")
            msg.exec_()
            return -2 # retornar -2 significa que não tem sala cadastrada selecionada

        # pegar o professor selecionado na lista
        item = self.listWidgetSalaProf.item(linha_selecionada)
        nome_professor = item.text()
        # procurar o objeto professor no "banco"
        professor = self.dados.get_professor_nome(nome_professor)
        # pegar o nome da sala
        item = self.listWidgetSalasCadastradas.item(sala_selecionada)
        sala = item.text()
        # adicionar o professor a sala selecionada
        self.dados.adicionar_professor_sala(professor, sala)
        # na GUI adicionar o nome do professor a lista de professores associados
        self.listWidgetSalaProfAssociados.addItem(nome_professor)



    #TODO: implementar a desasociacao de professor em futura versao
    def deassociar_professor_sala(self):
        pass


    def associar_aluno_sala(self):
        # testar se tem aluno selecionado na lista
        linha_selecionada = self.listWidgetSalaAluno.currentRow()

        if linha_selecionada == -1:
            msg = QMessageBox()
            msg.setText("Nenhum Aluno selecionado!")
            msg.exec_()
            return -1  # retornar -1 significa que nao tem professor selecionado

        # testar se tem sala selecionada na lista
        sala_selecionada = self.listWidgetSalasCadastradas.currentRow()

        if sala_selecionada == -1:
            msg = QMessageBox()
            msg.setText("Nenhuma sala cadastrada foi selecionada!")
            msg.exec_()
            return -2  # retornar -2 significa que não tem sala cadastrada selecionada

        # pegar o nome do aluno selecionado na lista
        item = self.listWidgetSalaAluno.item(linha_selecionada)
        nome_aluno = item.text()
        # procurar o objeto aluno no "banco"
        aluno = self.dados.get_aluno_nome(nome_aluno)
        # pegar o nome da sala
        item = self.listWidgetSalasCadastradas.item(sala_selecionada)
        sala = item.text()
        # adicionar o Aluno a sala selecionada
        self.dados.adicionar_aluno_sala(aluno, sala)
        # na GUI adicionar o nome do professor a lista de professores associados
        self.listWidgetSalaAlunoAssociados.addItem(nome_aluno)


    # TODO: implementar a desasociacao de professor em futura versao
    def deassociar_aluno_sala(self):
        pass


    """
    Metodos necessarios ao emprestimo/devolucao de chaves
    """

    def emprestar_chave(self):


        nome_sala = self.comboBoxSalasRegistro.currentText()
        nome_aluno = self.comboBoxAlunoRegistro.currentText()


        hoje = datetime.now()
        dia = hoje.day
        mes = hoje.month
        ano = hoje.year
        data = str(dia) + "/" + str(mes) +"/"+ str(ano)
        hora = hoje.hour
        minuto = hoje.minute
        hora_emprestimo = str(hora) + ":"+str(minuto)

        self.tableWidgetRegistros.insertRow(0)
        self.tableWidgetRegistros.setItem(0, 0, QTableWidgetItem(nome_sala))
        self.tableWidgetRegistros.setItem(0, 1, QTableWidgetItem(nome_aluno))
        self.tableWidgetRegistros.setItem(0, 2, QTableWidgetItem("Emprestada") )
        self.tableWidgetRegistros.setItem(0, 3, QTableWidgetItem(data))
        self.tableWidgetRegistros.setItem(0, 4, QTableWidgetItem(hora_emprestimo))
        self.tableWidgetRegistros.setItem(0, 5, QTableWidgetItem("--"))


    def devolver_chave(self):

        # TODO: A tabela deve ser atualizada para poder acomodar o caso em que um aluno pega a
        # chave em um dia e devolve em um dia diferente

        linha_selecionada = self.tableWidgetRegistros.currentRow()
        if linha_selecionada == -1:
            QMessageBox.information(self, "Erro", "Você precisa selecionar uma linha para devolução de chave")
        else:
            hoje = datetime.now()

            hora = hoje.hour
            minuto = hoje.minute
            hora_devolucao = str(hora) + ":" + str(minuto)
            self.tableWidgetRegistros.setItem(linha_selecionada, 2, QTableWidgetItem("Devolvida"))
            self.tableWidgetRegistros.setItem(linha_selecionada, 5, QTableWidgetItem(hora_devolucao))



    """
    Outros métodos ...
    """



    def limpar_campos(self):
        self.lineEditAlunoNome.clear()
        self.lineEditAlunoNome.setFocus()
        self.comboBoxCurso.setCurrentIndex(0)
        self.lineEditMatricula.clear()
        self.lineEditTelefone.clear()
        self.lineEditEmail.clear()
        #aba professor
        self.lineEditProfNome.clear()
        self.lineEditProfNome.setFocus()
        self.lineEditProfTelefone.clear()
        self.lineEditProfEmail.clear()


    def atualizar_dados_sala(self):
        #limpar lista de professores associados e de alunos associados

        self.listWidgetSalaProfAssociados.clear()
        self.listWidgetSalaAlunoAssociados.clear()

        # procurar o objeto sala na lista de salas
        sala_selecionada = self.listWidgetSalasCadastradas.currentRow()
        item = self.listWidgetSalasCadastradas.item(sala_selecionada)
        nome_sala = item.text()
        print("sala:", nome_sala)
        sala = self.dados.get_sala_nome(nome_sala)

        # pegar o nome dos professores associados e adicionar a lista
        lista_professores = sala.get_lista_professores()
        for i in lista_professores:
            self.listWidgetSalaProfAssociados.addItem(i.get_nome())


        # pegar o nome dos alunos associados e adicionar na lista
        lista_alunos = sala.get_lista_alunos()
        for i in lista_alunos:
            self.listWidgetSalaAlunoAssociados.addItem(i.get_nome())


    def povoar_combobox_alunoRegistro(self):

         # povoar a combobox com os alunos da sala correspondente
        self.comboBoxAlunoRegistro.clear()
        nome_sala = self.comboBoxSalasRegistro.currentText()
        sala = self.dados.get_sala_nome(nome_sala)
        lista_obj_alunos = sala.get_lista_alunos()
        if len(lista_obj_alunos) != 0:
            for al in lista_obj_alunos:
                self.comboBoxAlunoRegistro.addItem(al.get_nome())






# Metodos necessarios da aba sala


# metodos necessarios da aba Registro




# classes auxiliares
class AlunoDialog(QDialog, DialogAluno.Ui_DialogAluno):

    def __init__(self, parent=None):
        super(AlunoDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(" Editar Dados do aluno ")

        #conectar aos eventos Default
        self.pushButtonOk.clicked.connect(self.accept)
        self.pushButtonCancel.clicked.connect(self.reject)


class ProfDialog(QDialog, DialogProf.Ui_DialogProf):
    def __init__(self, parent=None):
        super(ProfDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Dados do professor ")

        #conectar aos eventos Default
        self.pushButtonOK.clicked.connect(self.accept)
        self.pushButtonCancel.clicked.connect(self.reject)






app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()