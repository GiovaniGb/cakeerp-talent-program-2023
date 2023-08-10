listaNumeros = []
listaNumeros.append(int(input("Digite o primeiro numero: ")))
listaNumeros.append(int(input("Digite o segundo numero: ")))
listaNumeros.append(int(input("Digite o terceiro numero: ")))

print(sorted(listaNumeros, reverse=True))