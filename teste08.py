import time 
import calendar

#print(time.asctime())
#tiks = time.time()
#print("Número de carrapatos desde 0h, 1º de janeiro de 1970: {:.1f}".format(tiks))
#localtime = time.asctime(time.localtime(time.time()))
#print(localtime)	

#Datahora = time.asctime(time.localtime(time.time()))
#print('A hora e data é {}'.format(Datahora))

#cal = calendar.month(2008,6)
#print('O caléndario está aqui:')
#print(cal)

i = 1
while i <= 4:
	nome = input('Qual é o seu nome: ')
	if nome != 'fim':
		print(nome)
	if nome == 'fim':
		break