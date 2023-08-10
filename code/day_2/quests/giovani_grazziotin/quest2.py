vetorIdade = []
vetorAltura = []
x=0
while x<5:
    vetorIdade.append(int(input(f"Digite a idade da pessoa {x+1}: ")))
    vetorAltura.append(float(input(f"Digite a altura da pessoa {x+1}: ")))
    x +=1

def inverteOrdem(vetor):
    x=0
    while x < int(len(vetor)/2):
        aux = vetor[x]
        vetor[x] = vetor[len(vetor)-1-x]
        vetor[len(vetor)-1-x] = aux
        x += 1

inverteOrdem(vetorIdade)
inverteOrdem(vetorAltura)

print("Vetor Altura: \n"+str(vetorAltura)+"\nVetor idade: \n"+str(vetorIdade))