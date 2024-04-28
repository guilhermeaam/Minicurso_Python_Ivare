#Tarefa 3:
# Faça um programa que leia uma string e imprima na tela a string 
# equivalente com a primeira letra de cada palavra em maiúscula. 
# Exemplo: “a casa amarela é bonita” → “A Casa Amarela É Bonita”.
# Enviar para o email: treinamento@ivare.com.br
# Nome do arquivo: nome_sobrenome.py
# Assunto: tarefa 3
print('Digite a string: Digite 0 para sair')
x=str(input().title())
while(x!='0'):
    print('A string equivalente é: '+x +'\n'+'Digite a string para achar a equivalente: Digite 0 para sair')
    x=str(input().title())