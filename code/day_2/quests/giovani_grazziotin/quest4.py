def soma(num1, num2, num3):
    resultado = num1+num2+num3
    print(f"A soma dos numeros: {resultado}")

try:
    num1 = int(input("Digite o primeiro numero inteiro: "))
    num2 = int(input("Digite o segundo numero inteiro: "))
    num3 = int(input("Digite o terceiro numero inteiro: "))
    soma(num1, num2, num3)
except:
    print("Você não digitou um numero inteiro!")    