import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget,  QMessageBox
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import * 

# Guilherme Afonso Alves Morais
# email: guilhermeafonso80@gmail.com

resultadox= ''
resultadoy= ''
operador = ''
conta= ''

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.dlg = uic.loadUi("calculadora.ui")
        self.dlg.show()
        self.dlg.pushButton_0.clicked.connect(self.imput0)
        self.dlg.pushButton_00.clicked.connect(self.imput00)
        self.dlg.pushButton_1.clicked.connect(self.imputUM)
        self.dlg.pushButton_2.clicked.connect(self.imput2)
        self.dlg.pushButton_3.clicked.connect(self.imput3)
        self.dlg.pushButton_4.clicked.connect(self.imput4)
        self.dlg.pushButton_5.clicked.connect(self.imput5)
        self.dlg.pushButton_6.clicked.connect(self.imput6)
        self.dlg.pushButton_7.clicked.connect(self.imput7)
        self.dlg.pushButton_8.clicked.connect(self.imput8)
        self.dlg.pushButton_9.clicked.connect(self.imput9)
        self.dlg.pushButton_vezes.clicked.connect(self.imputVezes)
        self.dlg.pushButton_divisao.clicked.connect(self.imputDivisao)
        self.dlg.pushButton_mais.clicked.connect(self.imputmais)
        self.dlg.pushButton_menos.clicked.connect(self.imputmenos)
        self.dlg.pushButton_raiz.clicked.connect(self.imputRaiz)
        self.dlg.pushButton_porcento.clicked.connect(self.imputPorcento)
        self.dlg.pushButton_igual.clicked.connect(self.imputIgual)
        self.dlg.pushButton_virgula.clicked.connect(self.imputvirgula)
        self.dlg.pushButton.clicked.connect(self.imputCE)

    def imputUM(self):
        global resultadox, resultadoy, operador
        if(operador==''):
            resultadox = resultadox + str('1')
            self.dlg.Resultado.setText(str(resultadox))
        else:
            resultadoy = resultadoy + str('1')
            self.dlg.Resultado.setText(str(resultadoy))
    
    def imput0(self):
        global resultadox, resultadoy, operador
        if(operador==''):
            resultadox = resultadox + str('0')
            self.dlg.Resultado.setText(str(resultadox))
        else:
            resultadoy = resultadoy + str('0')
            self.dlg.Resultado.setText(str(resultadoy))

    def imput00(self):
        global resultadox, resultadoy, operador
        if(operador==''):
            resultadox = resultadox + str('00')
            self.dlg.Resultado.setText(str(resultadox))
        else:
            resultadoy = resultadoy + str('00')
            self.dlg.Resultado.setText(str(resultadoy))

    def imput2(self):
        global resultadox, resultadoy, operador
        if(operador==''):
            resultadox = resultadox + str('2')
            self.dlg.Resultado.setText(str(resultadox))
        else:
            resultadoy = resultadoy + str('2')
            self.dlg.Resultado.setText(str(resultadoy))

    def imput3(self):
        global resultadox, resultadoy, operador
        if(operador==str('')):
            resultadox = resultadox + str('3')
            self.dlg.Resultado.setText(str(resultadox))
        else:
            resultadoy = resultadoy + str('3')
            self.dlg.Resultado.setText(str(resultadoy))

    def imput4(self):
        global resultadox, resultadoy, operador
        if(operador==''):
            resultadox = resultadox + str('4')
            self.dlg.Resultado.setText(str(resultadox))
        else:
            resultadoy = resultadoy + str('4')
            self.dlg.Resultado.setText(str(resultadoy))

    def imput5(self):
        global resultadox, resultadoy, operador
        if(operador==''):
            resultadox = resultadox + str('5')
            self.dlg.Resultado.setText(str(resultadox))
        else:
            resultadoy = resultadoy + str('5')
            self.dlg.Resultado.setText(str(resultadoy))
    
    def imput6(self):
        global resultadox, resultadoy, operador
        if(operador==''):
            resultadox = resultadox + str('6')
            self.dlg.Resultado.setText(str(resultadox))
        else:
            resultadoy = resultadoy + str('6')
            self.dlg.Resultado.setText(str(resultadoy))

    def imput7(self):
        global resultadox, resultadoy, operador
        if(operador==''):
            resultadox = resultadox + str('7')
            self.dlg.Resultado.setText(str(resultadox))
        else:
            resultadoy = resultadoy + str('7')
            self.dlg.Resultado.setText(str(resultadoy))
        
    def imput8(self):
        global resultadox, resultadoy, operador
        if(operador==''):
            resultadox = resultadox + str('8')
            self.dlg.Resultado.setText(str(resultadox))
        else:
            resultadoy = resultadoy + str('8')
            self.dlg.Resultado.setText(str(resultadoy))
        
    def imput9(self):
        global resultadox, resultadoy, operador
        if(operador==''):
            resultadox = resultadox + str('9')
            self.dlg.Resultado.setText(str(resultadox))
        else:
            resultadoy = resultadoy + str('9')
            self.dlg.Resultado.setText(str(resultadoy))

    def imputvirgula(self):
        def find(str, ch):
            indice = 0
            while indice < len(str):
                if str[indice] == ch:
                    return indice
                indice = indice + 1
            return -1

        global resultadox, resultadoy, operador, conta
        if(operador==''):
            if(find(resultadox,'.')==-1):
                resultadox = str(resultadox) + str('.')
                self.dlg.Resultado.setText(str(resultadox))
        else:
            if(find(resultadoy,'.')==-1):
                resultadoy = str(resultadoy) + str('.')
                self.dlg.Resultado.setText(str(resultadoy))
    
    def imputVezes(self):
        global resultadox, resultadoy, operador, conta
        if(resultadoy==''):
            operador = str('*')
            self.dlg.Resultado.setText(str('*'))
        else:
            conta= resultadox+ operador + resultadoy
            try:
                conta= eval(conta)
                self.dlg.Resultado.setText(str(conta))
                resultadox= str(conta)
                resultadoy= ''
                operador= str('*')
            except ZeroDivisionError:
                self.dlg.Resultado.setText(str("Erro: Divisão por 0"))
                resultadox= ''
                resultadoy= ''
                operador= str('')
        
    def imputDivisao(self):
        global resultadox, resultadoy, operador, conta
        if(resultadoy==''):
            operador = str('/')
            self.dlg.Resultado.setText(str('/'))
        else:
            conta= resultadox+ operador + resultadoy
            try:
                conta= eval(conta)
                self.dlg.Resultado.setText(str(conta))
                resultadox= str(conta)
                resultadoy= ''
                operador= str('/')
            except ZeroDivisionError:
                self.dlg.Resultado.setText(str("Erro: Divisão por 0"))
                resultadox= ''
                resultadoy= ''
                operador= str('')
        
    def imputmenos(self):
        global resultadox, resultadoy, operador, conta
        if(resultadoy==''):
            operador = str('-')
            self.dlg.Resultado.setText(str('-'))
        else:
            conta= resultadox+ operador + resultadoy
            try:
                conta= eval(conta)
                self.dlg.Resultado.setText(str(conta))
                resultadox= str(conta)
                resultadoy= ''
                operador= str('-')
            except ZeroDivisionError:
                self.dlg.Resultado.setText(str("Erro: Divisão por 0"))
                resultadox= ''
                resultadoy= ''
                operador= str('')
        
    def imputmais(self):
        global resultadox, resultadoy, operador, conta
        if(resultadoy==''):
            operador = str('+')
            self.dlg.Resultado.setText(str('+'))
        else:
            conta= resultadox+ operador + resultadoy
            try:
                conta= eval(conta)
                self.dlg.Resultado.setText(str(conta))
                resultadox= str(conta)
                resultadoy= ''
                operador= str('+')
            except ZeroDivisionError:
                self.dlg.Resultado.setText(str("Erro: Divisão por 0"))
                resultadox= ''
                resultadoy= ''
                operador= str('')
        
    def imputPorcento(self):
        global resultadox, resultadoy, operador, conta
        if(resultadoy==''):
            operador='/100'
            conta= resultadox+ operador
            conta= eval(conta)
            self.dlg.Resultado.setText(str(conta))
            resultadox= str(conta)
            operador= str('')
        else:
            try:
                conta= resultadox+ operador + resultadoy
                conta= eval(conta)
                resultadox= str(conta)
                resultado= resultadox+ '/100'
                resultado= eval(resultado)
                self.dlg.Resultado.setText(str(resultado))
                resultadox= str(resultado)
                operador= str('')
            except ZeroDivisionError:
                self.dlg.Resultado.setText(str("Erro: Divisão por 0"))
                resultadox= ''
                resultadoy= ''
                operador= str('')
            
    def imputRaiz(self):
        global resultadox, resultadoy, operador, conta
        if(resultadoy==''):
            operador='**0.5'
            conta= resultadox + operador
            conta= eval(conta)
            self.dlg.Resultado.setText(str(conta))
            resultadox= str(conta)
            operador= str('')
        else:
            try:
                conta= resultadox+ operador + resultadoy
                conta= eval(conta)
                resultadox= str(conta)
                resultado= resultadox+ '**0.5'
                resultado= eval(resultado)
                self.dlg.Resultado.setText(str(resultado))
                resultadox= str(resultado)
                operador= str('')
            except ZeroDivisionError:
                self.dlg.Resultado.setText(str("Erro: Divisão por 0"))
                resultadox= ''
                resultadoy= ''
                operador= str('')
          
    def imputIgual(self):
        global resultadox, resultadoy, operador, conta
        conta= resultadox+ operador + resultadoy
        try:
            conta= eval(conta)
            self.dlg.Resultado.setText(str(conta))
            resultadox= str(conta)
            resultadoy= ''
            operador= str('')
        except ZeroDivisionError:
            self.dlg.Resultado.setText(str("Erro: Divisão por 0"))
            resultadox= ''
            resultadoy= ''
            operador= str('')

    def imputCE(self):
        global resultadox, resultadoy, operador
        resultadoy= ''
        resultadox= ''
        operador= ''
        self.dlg.Resultado.setText(str('0'))
    


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()

    sys.exit(app.exec_())