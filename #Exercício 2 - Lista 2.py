#Exercício 2 - Lista 2

numeros = []

for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)


print(f"Números inseridos são: {numeros}")

lista_reversa = ', '.join(map(str, reversed(numeros)))
print(f"Esses são o números com a ordem invertida\n({lista_reversa})")