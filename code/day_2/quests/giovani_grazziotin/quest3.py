listaPerguntas = ["Telefonou para a vitima? ", "Esteve no local do crime? ", "Mora perto da vitima? ", "Devia para a vitima? ", "Já trabalhou com a vitima? "]
listaRespostas = []

print("Reponda com 1(sim) ou 0(não)\n")

x=0
while x<len(listaPerguntas):
    try:
        resposta = int(input(listaPerguntas[x]))
    except:
        print("Isso não é um número :<")
        continue    
    if resposta in (0,1):
        listaRespostas.append(resposta)
        x += 1
    else:
        print("Valor inválido.")
        continue

contagem = listaRespostas.count(1)
if contagem<2:
    print("Inocente!")
elif contagem==2:
    print("Suspeita!")
elif contagem>=3 and contagem<=4:
    print("Cúmplice!")
else:
    print("Assassino!")    