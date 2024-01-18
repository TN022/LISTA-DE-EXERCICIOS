#Exercício 3 - Lista 2

notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = (sum(notas)) / 4

for i, nota in enumerate(notas):
    print(f"A {i+1}ª nota é: {nota}")

print(f"A média de notas foi de: {media}")