#Exercício 8 - Lista 2
pessoas = []
alturas = []
idades = []

for i in range(5):
    pessoa = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    altura = float(input(f"Digite a altura da {i+1}ª pessoa: "))

    pessoas.append(pessoa)
    idades.append(idade)
    alturas.append(altura)

altura_reversa = alturas[::-1]
idade_reversa = idades[::-1]

print(altura_reversa)
print(idade_reversa)