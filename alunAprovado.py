notas = []
alunos = ["Matheus","Everton","Jussara","Bruna"]
alAprov = {"Matheus","Everton","Jussara","Bruna"}
materiaRuim = ("Português","Matemática","História","Geografia","Biologia","Inglês")
numMateria = 0
media = 0.0
presen = 0
total = 0
nomeAprov = ""
nomeRepr = ""
resp = ""
nome = ""
diaSemana = {"diaNum": 6 ,"diaSem":"Segunda"}
sisOnline = True
test = ""
             

print("ALUNO APROVADO OU REPROVADO")
print ("      ")
print ("      ")

while (resp!= "n"):
    print(f"Sistema online: {sisOnline}")
    print(f'Hoje é: {diaSemana["diaSem"]} dia {diaSemana["diaNum"]}')
    test = input("teste o teclado antes de começar pressionando varias teclas: ")
    print(f"A primeira letra é '{test[0]}', teste concluido!")
    print("")
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    presen = float(input("Digite a porcentagem de presença no ano: "))
    notas.append(float(input("digite a nota do primeiro bimestre: ")))
    notas.append(float(input("digite a nota do segundo bimestre: ")))
    notas.append(float(input("digite a nota do terceiro bimestre: ")))
    notas.append(float(input("digite a nota do quarto bimestre: ")))

    for notasb in notas:
        total = notasb + total    
        media = total / 4

    if(media >= 5 and presen >= 60 or media >= 7 and presen >= 70):
       nomeAprov = nome
       print(f"Parabéns {nomeAprov} você foi aprovado, sua média foi de {media} e sua presença foi de {presen}% ")
      
    else:
       nomeRepr = nome
       print(f"Que pena {nomeRepr},você não foi aprovado, sua média foi de {media} e sua presença foi de {presen}% ")
       from random import randint
       numMateria = (randint(0,5))
       print(f"Sua pior matéria foi a {materiaRuim[numMateria]}")
       

    resp = input("Deseja adicionar outro aluno ? (s) (n) ")

for nome in alunos:
    print("lista de alunos")
    print("Nome: ",nome)

print("lista de alunos ja aprovados")
print(alAprov)
print("Aluno reprovado")
print(alRepr)

