notasAluno = []
try:
    notasAluno.append(float(input("Digite a nota 1 do aluno (0 a 10): ")))
    notasAluno.append(float(input("Digite a nota 2 do aluno (0 a 10): ")))
except:
    print("Valor inválido")
    exit()

def calculaMedia(nota1, nota2):
    soma = nota1+nota2
    return soma/2

media = calculaMedia(notasAluno[0], notasAluno[1])
if media > 10:
    print("Você digitou algum valor fora do intervalo de 0 a 10!")
    exit()
if media<7:
    print(f"Reprovado com nota: {media}")
elif media>=7 and media<10:
    print(f"Aprovado com nota: {media}")
else: 
    print("Aprovado com distinção!")        