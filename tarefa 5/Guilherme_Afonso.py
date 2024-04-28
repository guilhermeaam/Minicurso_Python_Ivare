from os import curdir
from sqlite3.dbapi2 import SQLITE_SELECT, Connection, Cursor
import sys, sqlite3


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
resultado =''
contador= 1
cursorH= 1

class DBinit():
    def __init__(self):
        self.conn = sqlite3.connect("banco.db")
        self.c = self.conn.cursor()
        self.c.execute("""DROP TABLE IF EXISTS historico""")
        self.c.execute("""CREATE TABLE IF NOT EXISTS historico (contador INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, id INTEGER NOT NULL, x TEXT NOT NULL, operador TEXT NOT NULL, y TEXT, resultado TEXT NOT NULL, conta TEXT NOT NULL)""")
        self.c.close()
        self.conn.close()    

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.dlg = uic.loadUi("Guilherme_Afonso.ui")
        self.dlg.show()
        self.dlg.pushButton_0.clicked.connect(self.input0)
        self.dlg.pushButton_00.clicked.connect(self.input00)
        self.dlg.pushButton_1.clicked.connect(self.input1)
        self.dlg.pushButton_2.clicked.connect(self.input2)
        self.dlg.pushButton_3.clicked.connect(self.input3)
        self.dlg.pushButton_4.clicked.connect(self.input4)
        self.dlg.pushButton_5.clicked.connect(self.input5)
        self.dlg.pushButton_6.clicked.connect(self.input6)
        self.dlg.pushButton_7.clicked.connect(self.input7)
        self.dlg.pushButton_8.clicked.connect(self.input8)
        self.dlg.pushButton_9.clicked.connect(self.input9)
        self.dlg.pushButton_vezes.clicked.connect(self.inputVezes)
        self.dlg.pushButton_divisao.clicked.connect(self.inputDivisao)
        self.dlg.pushButton_mais.clicked.connect(self.inputMais)
        self.dlg.pushButton_menos.clicked.connect(self.inputMenos)
        self.dlg.pushButton_raiz.clicked.connect(self.inputRaiz)
        self.dlg.pushButton_porcento.clicked.connect(self.inputPorcento)
        self.dlg.pushButton_igual.clicked.connect(self.inputIgual)
        self.dlg.pushButton_virgula.clicked.connect(self.inputvirgula)
        self.dlg.pushButton.clicked.connect(self.inputCE)
        self.dlg.pushButton_UP.clicked.connect(self.upButton)
        self.dlg.pushButton_DOWN.clicked.connect(self.downButton) 
        self.dlg.pushButton_DEL.clicked.connect(self.delHistorico)
        self.dlg.pushButton_UPDATE.clicked.connect(self.upHistorico)
        self.bd = Banco_Comando()

    def delHistorico(self):
        global contador
        self.bd.del_historico(cursorH)
        self.dlg.Resultado.setText('Conta deletada!')
    
    def upHistorico(self):
        global contador
        self.up_historico(cursorH)

    def up_historico(self, cursorH):
        global contador, operador,resultadox, resultadoy, resultado
        try:
            self.conn = sqlite3.connect('banco.db')
            self.c = self.conn.cursor()
            self.c.execute("""SELECT x FROM historico WHERE contador=?""", [cursorH])
            row = self.c.fetchone()
            resultadox= str(row[0])
            resultadoy=''
            operador=''
            self.dlg.Resultado.setText(str((row[0])))
            self.c.close()
            self.conn.close()
        except Exception as e:
            print(e)

    def downButton(self):
        global contador, cursorH, resultadox, resultadoy, operador
        if(cursorH<contador-1):
            cursorH+=1
        if(cursorH<=contador):
            self.conn = sqlite3.connect('banco.db')
            self.c = self.conn.cursor()
            self.c.execute("""SELECT conta FROM historico WHERE contador=?""", [cursorH])
            row = self.c.fetchone()
            if(str(row)!='None'):
                self.dlg.Resultado.setText(str(row[0]))
                self.c.close()
                self.conn.close()
            else:
                if(cursorH<contador-1):
                    cursorH+=1
                self.conn = sqlite3.connect('banco.db')
                self.c = self.conn.cursor()
                self.c.execute("""SELECT conta FROM historico WHERE contador=?""", [cursorH])
                row = self.c.fetchone()
        self.conn = sqlite3.connect('banco.db')
        self.c = self.conn.cursor()
        self.c.execute("""SELECT resultado FROM historico WHERE contador=?""", [cursorH])
        row1 = self.c.fetchone()
        resultadox=str((row1[0]))
        resultadoy=''
        operador=''
        self.c.close()
        self.conn.close()

        return cursorH

    def upButton(self):
        global contador, cursorH, resultadoy, resultadox, operador
        if(cursorH>1):
            cursorH-=1
        if(cursorH<=contador):
            self.conn = sqlite3.connect('banco.db')
            self.c = self.conn.cursor()
            self.c.execute("""SELECT conta FROM historico WHERE contador=?""", [cursorH])
            row = self.c.fetchone()
            if(str(row)!='None'):
                self.dlg.Resultado.setText(str(row[0]))
                self.c.close()
                self.conn.close()
            else:
                if(cursorH<contador-1):
                    cursorH-=1
                self.conn = sqlite3.connect('banco.db')
                self.c = self.conn.cursor()
                self.c.execute("""SELECT conta FROM historico WHERE contador=?""", [cursorH])
                row = self.c.fetchone()
        self.conn = sqlite3.connect('banco.db')
        self.c = self.conn.cursor()
        self.c.execute("""SELECT resultado FROM historico WHERE contador=?""", [cursorH])
        row1 = self.c.fetchone()
        resultadox=str((row1[0]))
        resultadoy=''
        operador=''
        self.c.close()
        self.conn.close()
        return cursorH
    
    def inputValores(self, valor):
        global resultadox, resultadoy, operador
        if(operador==''):
            resultadox = resultadox + valor
            self.dlg.Resultado.setText(str(resultadox))
        else:
            resultadoy = resultadoy + valor
            self.dlg.Resultado.setText(str(resultadoy))

    def input1(self):
        self.inputValores('1')
    
    def input0(self):
        self.inputValores('0')

    def input00(self):
        self.inputValores('00')

    def input2(self):
        self.inputValores('2')

    def input3(self):
        self.inputValores('3')

    def input4(self):
        self.inputValores('4')

    def input5(self):
        self.inputValores('5')
    
    def input6(self):
        self.inputValores('6')

    def input7(self):
        self.inputValores('7')
        
    def input8(self):
        self.inputValores('8')
        
    def input9(self):
        self.inputValores('9')

    def inputvirgula(self):
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
    
    def inputOperador(self, operacional):
        global resultadox, resultadoy, operador, conta, contador
        if(resultadoy==''):
            operador = operacional
            self.dlg.Resultado.setText(operacional)
        else:
            conta=''
            conta= resultadox+ operador + resultadoy
            try:
                resultado= eval(conta)
                self.dlg.Resultado.setText(str(resultado))
                conta=conta+'='+str(resultado)
                self.bd.add_usuario(contador, resultadox, operador, resultadoy, resultado, conta)
                contador +=1
                resultadox= str(resultado)
                self.dlg.Resultado.setText(operacional)
                resultadoy= ''
                operador= operacional
            except ZeroDivisionError:
                self.dlg.Resultado.setText(str("Erro: Divisão por 0"))
                resultadox= ''
                resultadoy= ''
                operador= str('')

    def inputVezes(self):
        self.inputOperador('*')
        
    def inputDivisao(self):
        self.inputOperador('/')
        
    def inputMenos(self):
        self.inputOperador('-')
        
    def inputMais(self):
        self.inputOperador('+')
        
    def inputPorcentoRaiz(self, raizPorcento):
        global resultadox, resultadoy, operador, conta, resultado, contador
        if(resultadoy==''):
            operador=raizPorcento
            conta=''
            conta= resultadox + operador
            resultado= eval(conta)
            self.dlg.Resultado.setText(str(resultado))
            conta=conta+'='+str(resultado)
            self.bd.add_usuario(contador, resultadox, operador, resultadoy, resultado, conta)
            contador +=1
            resultadox= str(resultado)
            operador= str('')
        else:
            try:
                conta= resultadox+ operador + resultadoy
                conta= eval(conta)
                resultadox= str(conta)
                conta= resultadox+ raizPorcento
                resultado= eval(conta)
                self.dlg.Resultado.setText(str(resultado))
                conta=conta+'='+str(resultado)
                self.bd.add_usuario(contador,resultadox, raizPorcento, '', resultado, conta)
                contador +=1
                resultadox= str(resultado)
                operador= str('')
                resultadoy=''
                resultado=''
            except ZeroDivisionError:
                self.dlg.Resultado.setText(str("Erro: Divisão por 0"))
                resultadox= ''
                resultadoy= ''
                operador= str('')

    def inputPorcento(self):
        self.inputPorcentoRaiz('/100')
            
    def inputRaiz(self):
        self.inputPorcentoRaiz('**0.5')
          
    def inputIgual(self):
        global resultadox, resultadoy, operador, conta, resultado, contador
        conta= resultadox+ operador + resultadoy
        try:
            resultado= eval(conta)
            conta=conta + '=' + str(resultado)
            self.dlg.Resultado.setText(str(resultado))
            self.bd.add_usuario(contador, resultadox, operador, resultadoy, resultado, conta)
            contador +=1
            resultadox= str(resultado)
            resultadoy= ''
            operador= str('')
        except ZeroDivisionError:
            self.dlg.Resultado.setText(str("Erro: Divisão por 0"))
            resultadox= ''
            resultadoy= ''
            operador= str('')

    def inputCE(self):
        global resultadox, resultadoy, operador
        resultadoy= ''
        resultadox= ''
        operador= ''
        self.dlg.Resultado.setText(str('0'))
    
class Banco_Comando(object):
    def __init__(self):
        pass
    def add_usuario(self, contador, x, operador, y, resultado, conta):
        try:
            self.conn = sqlite3.connect('banco.db')
            self.c = self.conn.cursor()
            self.c.execute("""INSERT INTO historico(id, x, operador, y, resultado, conta) VALUES(?,?,?,?,?,?)""", (contador,x, operador, y, resultado, conta))
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception as e:
            print(e)

    def del_historico(self, id):
        try:
            self.conn = sqlite3.connect('banco.db')
            self.c = self.conn.cursor()
            self.c.execute("""DELETE FROM historico WHERE id=?""", [id])
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception as e:
            print(e)
            QMessageBox.warning(QMessageBox(), "Erro", "Dado não foi realizado com sucesso")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = DBinit()
    mainWindow = MainWindow()

    sys.exit(app.exec_())