#Exercício 10 - Lista 2

a = []
b = []

c = []

print("Insira os elementos do primeiro vetor:")
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º elemento: "))
    a.append(numero)

print("\nInsira os elementos do segundo vetor:")
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º elemento: "))
    b.append(numero)

for i in range(10):
    c.append(a[i])
    c.append(b[i])

print("\nTerceiro vetor intercalado:")
print(c)