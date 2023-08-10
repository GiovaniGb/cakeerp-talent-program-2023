try:
    letra = str(input("Digite seu sexo: F ou M\n"))
    if letra == 'M' or letra == 'm':
        print("Masculino!")
    elif letra == 'F' or letra == 'f':
        print("Feminino!")
    else:
        print("Sexo inválido!")
except:
    print("Não entendi o que você digitou...")                