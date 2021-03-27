print('=='*40)
print('=='*10,'CADASTRO HOSPITALAR','=='*19)
print('=='*40)
from time import sleep
nome = str(input('Digite seu nome completo, por favor: '))
idade = int(input('Qual é sua idade: '))
sexo = str(input('Qual é o seu sexo: ')).lower()
# -------------------- CONDIÇÃO PARA MENORES DE 18 ANOS -------------------------------------
if idade< 18: # Com o input pedindo a idade eu consigo indentificar qual condição ele vai. No caso essa aqui.
	# =================  Cadastro de menor de 18 anos  =======================
	print('=='*10,'REGISTRO DE MENOR','=='*19)
	print('Olá {}, tudo bem? \nVamos coletar alguns dados, pois você é menor de idade.'.format(nome))
	nome_pai = input('Nome do seu pai completo: ')
	nome_mae = input('Nome da sua mãe completo: ')
	data_nascimento = input('Sua data de nascimento(D/M/A): ')
	cpf = input('Digite seu CPF: ')
	sleep(2)
	print('=='*40)
	print('CADASTRO FEITO COM SUCESSO!')
	print('| Pai: {}'.format(nome_pai))
	print('| Mãe: {}'.format(nome_mae))
	print('| Data de nascimento: {}'.format(data_nascimento))
	print('| CPF: {}'.format(cpf))
	print()
	# -------------- CONDIÇÃO POR IDADE E SEXO ----------------------------------
	'''
	if sexo == 'masculino' and idade<= 10:
		print('ENCAMINHAMENTO PARA SETORES PARA O SEXO MASCULINO')
		print('Você foi encaminhado para o serto de crianças com a faixa etária até 10 anos')
	elif sexo == 'masculino' and idade>10 and idade<17:
		print('ENCAMINHAMENTO PARA SETORES PARA O SEXO MASCULINO')
		print('Você foi encaminhado para o serto de pré-adolecente')
	else:
		print('ENCAMINHAMENTO PARA SETORES PARA O SEXO MASCULINO')	
		print('Você foi encaminhado para o serto de jovens') 		
	'''
# ------------------- CONDIÇÃO PARA ADULTO ---------------------------------------------------
if idade>= 18 and idade <60:
	print('=='*10,'REGISTRO DE ADULTO','=='*19)
	print('Olá {}, tudo bem? Vamos fazer algumas perguntas.'.format(nome))
	cpf_adulto = input('Digite seu CPF: ')
	estadoCivil = input('Qual é seu estado civil? ')
	filhos = input('Tem filhos? ').upper()
	if filhos == 'SIM':
		Qfilhos = input('Quantos? ')
	doenca = input('Possui alguma doença infecciosa? ').upper()
	if doenca == 'SIM':
		doenca_infecciosa = input('Qual? ')
	print('Terminamos por aqui. Obrigado!')
	'''
	if sexo == 'masculino':
		print('Paciente {} adicionado com sucesso!'.format(sexo))
		hist = str(input('Você tem histórico de fumante na família ou você é? '))	
	elif sexo == 'feminino':
		print('Paciente {} adicionado com sucesso!'.format(sexo))
		hist = str(input('Você tem histórico de fumante na família ou você é? '))
	else:
		print('Dados incorretos....')
	'''
#  --------------------- CONDIÇÃO DE IDOSO ---------------------------------------------------