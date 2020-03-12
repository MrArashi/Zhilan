from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtXml
from ui import Ui_Dialog
import webbrowser

   
app = QtWidgets.QApplication(sys.argv)



Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
app.setWindowIcon(QtGui.QIcon('image\elf.png'))
    
#Logic

ui.pushButton.clicked.connect(lambda: webbrowser.open('https://signup.ru.leagueoflegends.com/ru/signup/redownload?type=new'))
ui.pushButton_2.clicked.connect(lambda: webbrowser.open('https://signup.ru.leagueoflegends.com/ru/signup/redownload?type=new'))

sys.exit(app.exec_())