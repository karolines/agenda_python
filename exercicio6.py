cargo = (input("Informe o seu cargo: "))
salario = float (input("Informe o seu salário: "))


nomeCargo = ""
if cargo == 100:
    percentual = 20
    nomeCargo = "Auxiliar Administrativo"

elif cargo == 101:
    percentual = 15
    nomeCargo = "Engenheiro"

elif cargo == 102:
    percentual = 10
    nomeCargo = "Gerente"

else:
    percentual = 0
    nomeCargo = "Cargo Invalido"



reajuste = salario * (percentual/100)
novo_salario = salario + reajuste

print(f"Cargo: {nomeCargo} \nSalário {salario:.2f}\nReajuste{reajuste:.2f}\nNovo Salário {novo_salario:.2f}")