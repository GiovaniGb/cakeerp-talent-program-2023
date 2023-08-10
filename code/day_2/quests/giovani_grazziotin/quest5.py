def somaImposto (taxaImposto, custo):
    imposto = (taxaImposto/100)*custo
    custo = custo+imposto
    return custo

try:
    taxaImposto = float(input("Digite a taxa de imposto em porcentagem: "))
    custo = float(input("Digite o custo do produto em reais: "))
    custo = somaImposto(taxaImposto, custo)
    print(f"O valor total do produto com imposto: R${custo}")
except:
    print("Voce não digitou um número!")    