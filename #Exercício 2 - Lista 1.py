#Exercício 2 - Lista 1

numeros = []

for i in range(2):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)


operacao = input("Digite qual operação você quer fazer entre os dois números (+, -, /, *): ")

if operacao == '+':
    print(int(sum(numeros)))
elif operacao == '-':
    print(int(numeros[0] - numeros[1]))
elif operacao == '/':
    print(int(numeros[0] / numeros[1]))
elif operacao == '*':
    print(int(numeros[0] * numeros[1]))
else:
    print("Operação inválida, use apenas (+, -, /, *)!")