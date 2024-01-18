#Exercício 7 - Lista 2

numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

def multiplicar():
    multiplicacao = 1
    for numero in numeros:
        multiplicacao *= numero
    return multiplicacao

multiplicacao = multiplicar()

print(f"A soma dos números inseridos é de: [{sum(numeros)}]")
print(f"A multiplicação entre os numeros inseridos é de: [{multiplicacao}]")
print(f"Os números que foram inseridos são: {numeros}")