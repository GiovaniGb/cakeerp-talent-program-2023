numeros = []
try:
    numeros.append(int(input("Digite um numero inteiro: ")))
    numeros.append(int(input("Digite outro numero inteiro: ")))
    print(f"Maior numero: {max(numeros)}")

except:
    print("Você não digitou um numero inteiro!")    