#Exercício 5 - Lista 2

numeros = []
par = []
impar = []

for i in range(20):
    numero = int(input(f'Digite o {i+1}º número: '))
    numeros.append(numero)
    if numero %2==0:
        par.append(numero)
    elif numero %2!=0:
        impar.append(numero)
    else:
        pass
print(f"Esses são os números inseridos: {numeros}.")
print(f"Esses são os números pares inseridos: {par}.")
print(f"Esses são os números ímpares inseridos: {impar}.")