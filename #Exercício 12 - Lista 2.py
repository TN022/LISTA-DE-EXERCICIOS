#Exercício 12 - Lista 2

alunos = []
idades = []
alturas = []

contador = 2
for i in range(contador):
    aluno = input(f"Digite o nome do {i+1}º Aluno: ")
    idade = int(input(f"Digite a idade do {i+1}º Aluno: "))
    altura = float(input(f"Digite a altura do {i+1}º Aluno: "))

    alunos.append(aluno)
    idades.append(idade)
    alturas.append(altura)

media_altura = sum(alturas) / contador

alunos_contagem = 0

for i in range(contador):
    if idades[i] > 13 and alturas[i] < media_altura:
        alunos_contagem += 1

print(f"A média de altura entre os alunos é de: {media_altura}")
print(f"A quantidade de alunos com mais de 13 anos que possuem altura inferior à média de alturas é de: {alunos_contagem}")