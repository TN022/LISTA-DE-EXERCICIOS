#Exercício 10 - Lista 1

numero = int(input('Digite o número para inversão de dígitos: '))
if numero >=100 and numero <=999:
    numero_str = str(numero)
    numero_invertido = numero_str[::-1]

    print(f"O número {numero} invertido é: {numero_invertido}")
else:
    print("Esse número não possui 3 dígitos.")