#Calculadora de teste
#calcula tabuada
numero = int(input("Informe a tabuada que deseja calcular "))
numerovezes = int(input("Informe a quantidade de multiplicações "))
for n in range(1, numerovezes + 1):
    resultado = n * numero
    print(f"{n} * {numero} = {resultado}")

