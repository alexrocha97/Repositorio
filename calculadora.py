# ------------- CALCULADORA --------------------
print('-==-'*20)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = input('Informe o sinal que deseja - ou +: ')

r = '';
# --- CÓDIGO DE SUBTRAÇÃO -------------------------
if op == '-':
	print('A subtração dos números foi:')
	r = n1 - n2
# --- CÓDIGO DE SOMA ------------------------------
if op == '+':
	print('A soma dos números foi:')
	r = n1 + n2
# --- CÓDIGO DE DIGITAÇÃO ERRADA ----------------

if op != '-' and op != '+':
	print('OPERAÇÃO NÃO SUPORTADA!')
print('-==-'*20)
# ------------- CALCULADORA --------------------

