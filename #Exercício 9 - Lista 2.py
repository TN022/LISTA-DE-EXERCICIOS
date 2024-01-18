#Exercício 9 - Lista 2

a = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º numero do vetor A: "))
    a.append(numero)

soma_dos_quadrados = (sum(a))**2

print(a)
print(f"A soma dos quadrados é de: {soma_dos_quadrados}")