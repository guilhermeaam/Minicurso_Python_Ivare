#Tarefa 2:Calcule a raiz quadrada aproximada de um número inteiro informado pelo usuário, 
# respeitando o erro máximo também informado pelo usuário. Não utilize funções predefinidas.
#Enviar para o email: treinamento@ivare.com.br
#Nome do arquivo: nome_sobrenome.py
#Assunto: tarefa 2

print('Digite o valor para achar a raiz: Digite "sair" para sair')
y = str(input())
while(y!='sair'):
    x = float(y)**0.5
    print('A raiz de '+str(y)+' é '+str(x)+'\n'+'Digite o valor para achar a raiz: Digite "sair" para sair')
    y = str(input())