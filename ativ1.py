print('-==-'*16)
print('=='*10,'Histórico do Aluno 01','=='*10)
nome = input('Digite seu nome: ')
aluno1 = float(input('Digite sua nota do primeiro semestre: '))
aluno2 = float(input('Digite sua nota do primeiro semestre: '))
media = (aluno1 + aluno2)/2
hist = ({'aluno':nome,'turma':'A','turno':'matutino'},[aluno1,aluno2])
print(hist[0])
print('Sua nota do primeiro semestre:',hist[1][0])
print('Sua média foi:',media)

if media < 5:
	print('Você precisa estudar mais...')
if media >= 5:
	print('Bom! Continue assim.')
print('-==-'*16)
