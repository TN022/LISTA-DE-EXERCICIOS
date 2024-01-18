#Exercício 11 - Lista 2

#Exercício 10 - Lista 2

a = []
b = []
c = []

d = []

print("Insira os elementos do primeiro vetor:")
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º elemento: "))
    a.append(numero)

print("\nInsira os elementos do segundo vetor:")
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º elemento: "))
    b.append(numero)

print("\nInsira os elementos do terceiro vetor:")
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º elemento: "))
    c.append(numero)


for i in range(10):
    d.append(a[i])
    d.append(b[i])
    d.append(c[i])

print("\nQuarto vetor intercalado pelos vetores 1 , 2 e 3:")
print(d)