#Exercício 4 - Lista 1

numeros = []

contador = (int(input("Quantos números serão inseridos? ")))

for i in range(contador):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

media = (sum(numeros))/ contador

print(f"A média aritmética entre os {contador} números fornecidos é de: {media}")