from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import sys, shutil, os

from grafico import gerarGrafico
from Arduino import Arduino, findArduino
from Instruments import PowerSupply, Multimeter
from teste import Teste
# usei essas listas pra
graficos = [
    # "gráfico 1","gráfico 2", "gráfico 3"
]
tabelas = [
    # "tabela 1",'tabela 2', 'tabela 3', 'tabela 4'
]
types = ["csv", "xls", "xlsx", "json"]
porta = findArduino()
def getPath(pasta):
    my_os = sys.platform
    if my_os == 'win32':
        return '.\\'+pasta+'\\'
curr_lim =  0.01
volt_lim = 5.

class Ui_MainWindow(object):
    # Criando os componentes
    def setupUi(self, MainWindow):
        MainWindow.resize(560, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 560, 570))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.tabWidget.setFont(font)
        self.tab = QtWidgets.QWidget()
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 510, 230))

        font75 = QtGui.QFont()
        font75.setFamily("Arial")
        font75.setPointSize(12)
        font75.setBold(True)
        font75.setWeight(75)

        self.groupBox.setFont(font75)
        self.tipo_v = QtWidgets.QComboBox(self.groupBox)
        self.tipo_v.setGeometry(QtCore.QRect(260, 120, 80, 30))

        self.tipo_v.setFont(font75)
        self.tipo_v.setObjectName("tipo_v")
        self.tipo_v.addItem("")
        self.tipo_v.addItem("")
        self.tipo_v.addItem("")
        self.input_c = QtWidgets.QLineEdit(self.groupBox)
        self.input_c.setGeometry(QtCore.QRect(30, 60, 210, 30))

        self.input_c.setFont(font75)
        self.input_c.setObjectName("input_c")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 110, 30))

        font50 = QtGui.QFont()
        font50.setFamily("Arial")
        font50.setPointSize(12)
        font50.setBold(False)
        font50.setWeight(50)

        self.label.setFont(font50)
        self.label_voltagem = QtWidgets.QLabel(self.groupBox)
        self.label_voltagem.setGeometry(QtCore.QRect(20, 90, 110, 30))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.label_voltagem.setFont(font50)
        self.tipo_a = QtWidgets.QComboBox(self.groupBox)
        self.tipo_a.setGeometry(QtCore.QRect(260, 60, 80, 30))

        self.tipo_a.setFont(font75)
        self.tipo_a.setObjectName("tipo_a")
        self.tipo_a.addItem("")
        self.tipo_a.addItem("")
        self.tipo_a.addItem("")
        self.input_v = QtWidgets.QLineEdit(self.groupBox)
        self.input_v.setGeometry(QtCore.QRect(30, 120, 210, 30))

        self.input_v.setFont(font75)
        self.input_v.setObjectName("input_v")
        self.label_n_sensor = QtWidgets.QLabel(self.groupBox)
        self.label_n_sensor.setGeometry(QtCore.QRect(20, 150, 170, 30))

        self.label_n_sensor.setFont(font50)
        self.n_sensor = QtWidgets.QComboBox(self.groupBox)
        self.n_sensor.setGeometry(QtCore.QRect(30, 180, 80, 30))

        self.n_sensor.setFont(font75)
        self.n_sensor.setObjectName("n_sensor")
        self.n_sensor.addItem("")
        self.n_sensor.addItem("")
        self.n_sensor.addItem("")
        self.btn_iniciar = QtWidgets.QPushButton(self.tab)
        self.btn_iniciar.setGeometry(QtCore.QRect(140, 420, 260, 40))
        self.btn_iniciar.clicked.connect(self.actionIniciar)

        self.btn_iniciar.setFont(font75)
        self.btn_iniciar.setObjectName("btn_iniciar")
        self.btn_interromper = QtWidgets.QPushButton(self.tab)
        self.btn_interromper.setGeometry(QtCore.QRect(280, 470, 150, 40))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)

        self.btn_interromper.setFont(font)
        self.btn_interromper.setObjectName("btn_interromper")
        self.btn_resetar = QtWidgets.QPushButton(self.tab)
        self.btn_resetar.setGeometry(QtCore.QRect(100, 470, 150, 40))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)

        self.btn_resetar.setFont(font)
        self.btn_resetar.setObjectName("btn_resetar")
        self.btn_resetar.clicked.connect(self.actionResetar)

        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 250, 510, 150))

        self.groupBox_3.setFont(font75)
        self.input_caminho = QtWidgets.QLineEdit(self.groupBox_3)
        self.input_caminho.setGeometry(QtCore.QRect(30, 70, 360, 30))

        self.input_caminho.setFont(font50)
        self.input_caminho.setObjectName("input_caminho")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 110, 30))

        self.label_3.setFont(font50)
        self.tipo_file = QtWidgets.QComboBox(self.groupBox_3)
        self.tipo_file.setGeometry(QtCore.QRect(400, 70, 70, 30))

        self.tipo_file.setFont(font50)
        self.tipo_file.setObjectName("tipo_file")
        for i in range(len(types)):
            self.tipo_file.addItem("")

        self.label_avisos = QtWidgets.QLabel(self.groupBox_3)
        self.label_avisos.setGeometry(QtCore.QRect(20, 120, 450, 20))

        self.label_avisos.setFont(font50)
        self.label_avisos.setMidLineWidth(0)
        self.label_avisos.setText("")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 10, 510, 140))

        self.groupBox_4.setFont(font75)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(20, 60, 200, 30))
        self.label_8.setFont(font50)

        self.btn_gerar_tabela = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_gerar_tabela.setGeometry(QtCore.QRect(400, 90, 90, 30))
        self.btn_gerar_tabela.setObjectName("btn_gerar_tabela")
        self.btn_gerar_tabela.clicked.connect(self.actionGerar)

        self.select_tabela = QtWidgets.QComboBox(self.groupBox_4)
        self.select_tabela.setGeometry(QtCore.QRect(30, 90, 360, 30))
        # for i in range(len(tabelas)):
        #     self.select_tabela.addItem("")

        self.btn_importar_tabela = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_importar_tabela.setObjectName("btn_importar_tabela")
        self.btn_importar_tabela.setGeometry(QtCore.QRect(20, 30, 201, 28))
        self.btn_importar_tabela.clicked.connect(self.importarTabela)

        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 160, 510, 120))

        self.groupBox_5.setFont(font75)
        # self.groupBox_5.setObjectName("groupBox_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 140, 30))
        self.label_9.setFont(font50)

        self.select_grafico = QtWidgets.QComboBox(self.groupBox_5)
        self.select_grafico.setGeometry(QtCore.QRect(30, 70, 360, 30))
        self.select_grafico.setObjectName("select_grafico")
        # for i in range(len(graficos)):
        #     self.select_grafico.addItem("")

        self.btn_mostrar = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_mostrar.setGeometry(QtCore.QRect(400, 70, 90, 30))
        self.btn_mostrar.clicked.connect(self.actionMostrar)

        self.label_img_grafico = QtWidgets.QLabel(self.tab_2)
        self.label_img_grafico.setGeometry(QtCore.QRect(40, 290, 480, 240))
        self.label_img_grafico.setAutoFillBackground(False)
        self.label_img_grafico.setText("")
        # self.label_img_grafico.setPixmap(
        #     QtGui.QPixmap("/home/lanerson/Downloads/prog/graficos/Figure 1.png")
        # )
        self.label_img_grafico.setScaledContents(True)
        # self.label_img_grafico.setObjectName("label_img_grafico")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # self.serial = Arduino(porta)
        # self.font = PowerSupply(curr_lim,volt_lim)
        # self.multimeter = Multimeter(self.serial)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sensor"))
        self.groupBox.setTitle(_translate("MainWindow", "Dados de Entrada"))
        self.tipo_v.setItemText(0, _translate("MainWindow", "V"))
        self.tipo_v.setItemText(1, _translate("MainWindow", "mV"))
        self.tipo_v.setItemText(2, _translate("MainWindow", "µV"))
        self.label.setText(_translate("MainWindow", "Corrente"))
        self.label_voltagem.setText(_translate("MainWindow", "Voltagem"))
        self.tipo_a.setItemText(0, _translate("MainWindow", "A"))
        self.tipo_a.setItemText(1, _translate("MainWindow", "mA"))
        self.tipo_a.setItemText(2, _translate("MainWindow", "µA"))
        self.label_n_sensor.setText(_translate("MainWindow", "Número de sensores"))
        self.n_sensor.setItemText(0, _translate("MainWindow", "15"))
        self.n_sensor.setItemText(1, _translate("MainWindow", "10"))
        self.n_sensor.setItemText(2, _translate("MainWindow", "5"))
        self.btn_iniciar.setText(_translate("MainWindow", "Iniciar"))
        self.btn_interromper.setText(_translate("MainWindow", "Interromper"))
        self.btn_resetar.setText(_translate("MainWindow", "Resetar valores"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Salvamento"))
        self.label_3.setText(_translate("MainWindow", "Nome"))
        for i, tipo in enumerate(types):
            self.tipo_file.setItemText(i, _translate("MainWindow", tipo))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Medir")
        )
        self.groupBox_4.setTitle(_translate("MainWindow", "Gerar Gráfico"))
        self.label_8.setText(_translate("MainWindow", "Selecione a fonte de dados"))
        self.btn_gerar_tabela.setText(_translate("MainWindow", "Gerar"))
        self.btn_importar_tabela.setText(_translate("MainWindow", "Importar tabela"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Visualizar Gráfico"))
        self.label_9.setText(_translate("MainWindow", "Selecione o gráfico"))
        self.btn_mostrar.setText(_translate("MainWindow", "Mostrar"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Visualizar")
        )

    # método para atualizar os itens do select
    def setItems(self, pai, filhos):
        _translate = QtCore.QCoreApplication.translate
        pai.clear()
        for i, filho in enumerate(filhos):
            pai.addItem("")
            pai.setItemText(i, _translate("MainWindow", filho))

    # criei mais pra confirmar as coisas
    def popUp(self, modo):
        msg = QMessageBox()
        if modo == "Iniciar":
            msg.setWindowTitle("bora")
            msg.setText("Tem certeza que deseja continuar?")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        elif modo == "Error":
            msg.setWindowTitle("Erro")
            msg.setText("Extensão do arquivo não suportada")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
        elif modo == "Resetar":
            msg.setWindowTitle("bora")
            msg.setText("Tem certeza que deseja continuar?")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        elif modo == "Interromper":
            pass

        x = msg.exec_()
        return x

    # especifico das tabelas
    def setTabelas(self):
        pasta = "/".join(sys.argv[0].split("/")[:-1]) + "/tabelas/"
        # Lista todos os arquivos na pasta
        arquivos = os.listdir(pasta)
        # Filtra apenas os arquivos (exclui diretórios)
        arquivos = [
            arquivo
            for arquivo in arquivos
            if os.path.isfile(os.path.join(pasta, arquivo))
        ]
        # Imprime a lista de arquivos
        # tabelas = arquivos.copy()
        self.setItems(self.select_tabela, arquivos)

    # especifico dos gráficos
    def setGraficos(self):
        pasta = "/".join(sys.argv[0].split("/")[:-1]) + "/graficos/"
        # Lista todos os arquivos na pasta
        arquivos = os.listdir(pasta)
        # Filtra apenas os arquivos (exclui diretórios)
        arquivos = [
            arquivo
            for arquivo in arquivos
            if os.path.isfile(os.path.join(pasta, arquivo))
        ]
        # Imprime a lista de arquivos
        self.setItems(self.select_grafico, arquivos)

    def actionIniciar(self):
        # criar pop up pro cara confirmar
        
        resp = self.popUp("Iniciar")
        if resp == QMessageBox.Ok:
            print(self.tipo_file.currentText())
                

        else: print('not ok')
        #       colocar avisos
        # coletar valores
        # acionar medição

        pass

    def actionResetar(self):
        self.input_c.setText("")
        self.input_v.setText("")
        self.input_caminho.setText("")
        self.tipo_a.setCurrentIndex(0)
        self.tipo_v.setCurrentIndex(0)
        self.n_sensor.setCurrentIndex(0)
        self.tipo_file.setCurrentIndex(0)

    def actionInterromper(self):
        # parar medição
        pass

    def importarTabela(self):
        def abrirDialogo():
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getOpenFileName(
                self.groupBox_4,
                "Escolher Arquivo",
                "",
                "Todos os Arquivos (*)",
                options=options,
            )
            if file_path:
                print("Arquivo selecionado:", file_path)
                return file_path

        file = abrirDialogo()
        if not (file):
            return
        if not (file.split(".")[-1] in types):
            self.popUp("Error")
            return 0
        path = "/".join(sys.argv[0].split("/")[:-1]) + "/tabelas/" + file.split("/")[-1]
        try:
            shutil.copy2(file, path)
            # print(f"Cópia segura de '{file}' para '{path}' foi concluída com sucesso.")
        except PermissionError:
            print(f"Você não tem permissão para acessar o arquivo '{file}'.")
        except Exception as e:
            print(f"Erro ao copiar o arquivo: {str(e)}")
        self.setTabelas()

    def actionGerar(self):
        # ver qual tabela foi selecionada
        # acionar geração de gráfico
        self.setGraficos()

    def actionMostrar(self):
        # ver qual gráfico foi selecionado
        text = self.select_grafico.currentText()
        path = pasta = "/".join(sys.argv[0].split("/")[:-1]) + "/graficos/" + text
        self.label_img_grafico.setPixmap(QtGui.QPixmap(path))
        # mostrar o gráfico no label
        pass
    def fazerMedicao(self):
        self.font.powerSupplyOpen()
        c = self.input_c.strip()
        v = self.input_v.strip()
        c = int(c) if c.isdigit() else False
        v = int(v) if v.isdigit() else False
        if( c and v):
            file = self.input_caminho.text()
            type = self.tipo_file.currentText()
            self.multimeter.readValues()
        # self.multimeter.readValues()

        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setTabelas()
    ui.setGraficos()
    MainWindow.show()
    sys.exit(app.exec_())
