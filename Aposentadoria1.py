import time
print('-==-'*18)
print('=='*10,'VERIFICAÇÃO DE APOSENTADORIA','=='*10)

nome = input('Por favor, escreva seu nome completo: ')
idade = int(input('Quantos anos você tem? '))
sexo = input('Qual sexo você é? ')
rendaAtual = float(input('Qual é o valor da sua renda atualmente? '))

print('Carregando...')

time.sleep(2)

#print(nome,idade,sexo,rendaAtual)

mas = (rendaAtual * 75)/100
fem = (rendaAtual * 70)/100

nov1 = 60 - idade
nov2 = 65 - idade

print('-==-'*18)

if sexo == 'masculino' and idade >= 65: # calculo masculino
	print(nome,'sua aposentadoria foi liberada no valor R$ {}'.format(mas))

if sexo == 'feminino' and idade >= 60:
	print(nome,'sua aposentadoria foi liberada no valor R$',fem)

if idade < 60 and sexo == 'feminino':
	print(nome,',sua aposentadoria não foi autorizada, faltam',nov1,'anos')

if idade < 65 and sexo == 'masculino':
	print(nome,',sua aposentadoria não foi autorizada, faltam',nov2,'anos')

if rendaAtual <= 0:
	print('ERRO!Você precisa preencher corretamete o campo da Renda Atual')
print('-==-'*18)
