from selenium.webdriver.common.by import By
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
from pypdf import PdfReader
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from file_manager import *
import os
import time



def download_pdf_di(driver, numero):
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    arquivos = {
        "di": os.path.join(download_dir, f"Desenhos_Industriais{numero}.pdf"),
        "m": os.path.join(download_dir, f"Marcas{numero}.pdf"),
        "p": os.path.join(download_dir, f"Patentes{numero}.pdf")
    }
    driver.get(f"https://revistas.inpi.gov.br/pdf/Marcas{numero}.pdf")
    time.sleep(3)
    driver.get(f"https://revistas.inpi.gov.br/pdf/Desenhos_Industriais{numero}.pdf")
    time.sleep(3)
    driver.get(f"https://revistas.inpi.gov.br/pdf/Patentes{numero}.pdf")

    while True:
        todos_baixados = True
        for caminho in arquivos.values():
            # Verifica se o arquivo existe E se ele não está sendo baixado (nome temporário)
            if not os.path.exists(caminho) or caminho.endswith('.crdownload'):
                todos_baixados = False
                break

        if todos_baixados:
            break

        time.sleep(3)
        print("Aguardando downloads...")

    print("Download concluído")
    return


def get_num(driver):

    driver.get("https://revistas.inpi.gov.br/rpi/")
    item = driver.find_element(By.CLASS_NAME, "warning")
    lista = []
    count = 0
    for x in item.text:
        count+=1
        if count > 4:
            break
        lista.append(x)
    separator = ""
    numero = separator.join(lista)
    time.sleep(1)
    return numero




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 438)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(420, 70, 161, 61))
        self.runButton.setObjectName("runButton")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(190, -50, 331, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.resultsLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultsLabel.setGeometry(QtCore.QRect(10, 150, 631, 261))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.resultsLabel.setFont(font)
        self.resultsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultsLabel.setObjectName("resultsLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.name_input = QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(20, 70, 200, 30))
        self.name_input.setObjectName("name_input")

        self.runButton.clicked.connect(self.onClick)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def onClick(self):
        make_dir()
        options = Options()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        self.resultsLabel.setText("Carregando aguarde...")
        numero = get_num(driver)

        download_pdf_di(driver, numero)
        driver.close()

        move_pdf(numero)

        label = self.extract_text(numero)
        self.resultsLabel.setText(label)

    def extract_text(self, numero):
        file_list = []
        message = []
        for x in os.listdir(os.path.join(os.path.expanduser("~"), "Desktop", "pdf_inpi")):
            if numero in x:
                file_list.append(x)

        for file in file_list:
            path = os.path.join(os.path.expanduser("~"), "Desktop", "pdf_inpi", file)
            reader = PdfReader(path)
            condition = self.name_input.text()
            condition = condition.lower()
            pages = reader.pages
            trigger_place = []
            page_num = 0

            for y in pages:
                page_num += 1
            for x in range(page_num):
                # print(x)
                page = reader.pages[x]
                text = page.extract_text()
                text = text.lower()
                if condition in text:
                    corrected_num = x + 1
                    trigger_place.append(corrected_num)
            if trigger_place:

                message.append(f"No documento '{file}', '{condition}' aparece nas seguintes páginas:\n{trigger_place}")

                continue
            else:
                message.append(f"'{condition}' não aparece no documento '{file}'")
                os.remove(path)
                continue

        label = "\n".join(message)

        print("Todos os arquivos foram analisados")
        return label



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.runButton.setText(_translate("MainWindow", "Start"))
        self.titleLabel.setText(_translate("MainWindow", "INPI PDF ANALISER"))
        self.resultsLabel.setText(_translate("MainWindow", "Os resultados aparecerão aqui"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())