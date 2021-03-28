# -------- Controle de dados de usinagem --------------
inventario = []
tolerancia_da_peca = []
resp = 'sim'
while resp == 'sim':
    descrica_da_peca = [input('Nome da peça: '),
                        float(input('Diâmentro: ')),
                        float(input('Comprimento(mm): '))]
    inventario.append(descrica_da_peca)

    perg_de_tolerancia = input('Essa peça tem tolerância? ').lower()

    if perg_de_tolerancia == 'sim':
        medida_tolerancia = [float(input('Comprimento: ')),
                             float(input('Diâmentro 01: ')),
                             float(input('Diâmentro 02: '))]
        tolerancia_da_peca.append(medida_tolerancia)
        print('==' * 40)
    '''
    nome_peca.append(input("Nome da peça: ")) # Registrar o nome da peça que está fazendo no cnc
    compri.append(float(input('Comprimento(mm): '))) # Aqui você registra o comprimento da peça
    diam.append(float(input('Diâmentro(mm): ')))
    
    perg_de_tolerancia = input('\nEssa peça tem tolerância? ').lower() # Um imput para saber se a peça tem tolêrancia precisa

    if perg_de_tolerancia == 'sim':
        medida_tolerancia = [float(input('Comprimento: ')),
                             float(input('Diâmentro 01: ')),
                             float(input('Diâmentro 02 :'))]
        tolerancia_da_peca.append(medida_tolerancia)
    '''
    resp = input('Deseja cadastrar outra peça? ').lower()

for elemento in inventario:
    print('=='*40)
    print('Nome da peça: ', elemento[0])
    print('Diâmentro: ', elemento[1])
    print('Comprimento(mm): ', elemento[2])

for tolerancia in tolerancia_da_peca:
    print('-----Tolerância de Peças registradas-----')
    print('Comprimento: ', tolerancia[0])
    print('Diâmetro 01: ', tolerancia[1])
    print('Diâmetro 02: ', tolerancia[2])
'''
for indice in tolerancia_da_peca:
    print('Comprimento...:', indice[0])
    print('Diâmentro 01..:', indice[1])
    print('Diâmetro 02...:', indice[2])
'''
print('=='*40)

