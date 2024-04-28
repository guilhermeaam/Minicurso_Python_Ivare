# Tarefa 1:
# Leia um número decimal (até 3 dígitos) e escreva o seu equivalente em numeração romana.
# 1 = I, 5 = V, 10 = X, 50 = L, 100 = C, 500 = D, 1.000 = M.
# Enviar para o email: treinamento@ivare.com.br
# Nome do arquivo: nome_sobrenome.py
# Assunto: tarefa 1

print('Digite o valor para achar o equivalente romano: Digite "sair" para sair')
y = str(input())
z = list(map(str, y.strip()))
romana=str('')
i=str('I')
v=str('V')
x=str('X')
l=str('L')
c=str('C')
d=str('D')
m=str('M')
def conferirUnidades(unidade):
            global romana
            u = unidade
            if(0<u and u<4):
                for h in range(u):
                    romana = romana+i
            elif(u==4):
                romana=romana+i+v
            elif(u==5):
                romana=romana+v
            elif(5<u<9):
                e=-(5-u)
                romana=romana+v
                for e in range(e):
                    romana= romana+i
            elif(u==9):
                romana= romana+i+x

def conferirDezenas(dezena):
    global romana
    dezenas = dezena
    if(0<dezenas and dezenas<4):
        for h in range(dezenas):
            romana = romana+x
    elif(dezenas==4):
        romana=romana+x+l
    elif(dezenas==5):
        romana=romana+l
    elif(5<dezenas<9):
        e=-(5-dezenas)
        romana=romana+l
        for e in range(e):
            romana= romana+x
    elif(dezenas==9):
        romana= romana+x+c

def conferirCentenas(centena):
    global romana
    centenas = centena
    if(0<centenas and centenas<4):
        for h in range(centenas):
            romana = romana+c
    elif(centenas==4):
        romana=romana+c+d
    elif(centenas==5):
        romana=romana+d
    elif(5<centenas<9):
        e=-(5-centenas)
        romana=romana+d
        for e in range(e):
            romana= romana+c
    elif(centenas==9):
        romana= romana+c+m

while(y!='sair'):
    if(int(y)<1000):
        if(len(z)==3):
            conferirCentenas(int(z[0]))
            conferirDezenas(int(z[1]))   
            conferirUnidades(int(z[2]))

        elif (len(z)==2):
            conferirDezenas(int(z[0]))
            conferirUnidades(int(z[1]))
        
        elif (len(z)==1): 
            conferirUnidades(int(z[0]))

        print('O numero em romano é '+ romana)
        print('Digite o valor para achar o equivalente romano: Digite "sair" para sair')
        romana=''
        y = str(input())
        z = list(map(str, y.strip()))
    else:
        print('Digite um valor menor ou igual a 999')