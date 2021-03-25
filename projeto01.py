print('=='*40)
print('=='*10,'CADASTRO HOSPITALAR','=='*19)
print('=='*40)
nome = str(input('Digite seu nome completo, por favor: '))
idade = int(input('Qual é sua idade: '))
sexo = str(input('Qual é o seu sexo: ')).lower()
if idade<= 18:
	print('=='*5,'Ala de menores','=='*5)
	print('Olá {}, tudo bem? Vamos fazer algumas perguntas.'.format(nome))
	vacina = input('Você já tomou a vacina de Sarampo? ').upper()
	if vacina == 'SIM':
		print('Você não precisa da vacina.')
	else:
		print('Por favor, vá até a sala 144A e registre seu nome para tomar a vacina.')
if idade> 18 and idade <60:
	print('=='*5,'Ala de adultos','=='*5)
	print('Olá {}, tudo bem? Vamos fazer algumas perguntas.'.format(nome))
	if sexo == 'masculino':
		print('Paciente {} adicionado com sucesso!'.format(sexo))
		hist = str(input('Você tem histórico de fumante na família ou você é? '))	
	elif sexo == 'feminino':
		print('Paciente {} adicionado com sucesso!'.format(sexo))
		hist = str(input('Você tem histórico de fumante na família ou você é? '))
	else:
		print('Dados incorretos....')