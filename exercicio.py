########################### ATIVIDADE ################################
print('-==-'*20)
print('-=-'*10,'VERIFICADOR DE MÉDIA DO ALUNO','-=-'*10)
print('Olá! Vou analisar seu histórico de notas desse ano.')
import time
nome = input('Escreva seu nome, por favor: ')
num = 1
nota = []
######### ESTRUTURA DE REPETIÇÃO COM WHILE PARA COLETAR AS NOTAS #####
while num <= 4:
	nota += [float(input(f'Informe as notas: '))]
	#print('Nota', nota)
	num = num + 1
	soma = 0
#########  ESTRUTURA PARA COLETAR AS NOTAS E SOMAR COM FOR/IN ########
	for i in nota:
		soma = soma + i
		media = soma/4
######### USO DO IF/ELIF E ELSE ####################################
print('-==-'*20)
print('Carregando...')
time.sleep(2)
if media >= 7:
	print(f'{nome}, sua média é {media}')
	print('Parabéns! Você está aprovado.')
elif media < 7 and media >= 5:
    print(f'{nome}, sua média é {media}')
    print('Você está em recuperação, mas não fique desanimado, você pode passar!')
else:
    print(f'{nome}, sua média é {media}')
    print('Desculpe..você terá que repetir de série. Você foi reprovado!')
print('-==-'*20)
