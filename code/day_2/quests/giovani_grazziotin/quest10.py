atualSalario = float(input("Digite o salário atual: "))
antigoSalario = atualSalario

if atualSalario<= 280:
    atualSalario *= 1.2
elif atualSalario>280 and atualSalario <=700:
    atualSalario *= 1.5
elif atualSalario>700 and atualSalario<=1500:
    atualSalario *= 1.1
else:
    atualSalario *= 1.05

print(f"Salario antes do reajuste: R${antigoSalario}")
print(f"Percentual de aumento aplicado: {(atualSalario/antigoSalario)*100-100}%") 
print(f"O valor do aumento: R${atualSalario-antigoSalario}")
print(f" Novo salario, apos aumento: R${atualSalario}")               