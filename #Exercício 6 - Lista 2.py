#Exercício 6 - Lista 2

contador = 3

alunos = []
medias = []
aprovados = 0

for i in range(contador):
    aluno = (input('Digite o nome do aluno: '))
    nota1 = float(input(f'Digite a primeira nota do aluno {aluno}: '))
    nota2 = float(input(f'Digite a segunda nota do aluno {aluno}: '))
    nota3 = float(input(f'Digite a terceira nota do aluno {aluno}: '))
    nota4 = float(input(f'Digite a quarta nota do aluno {aluno}: '))

    media = (nota1 + nota2 + nota3 + nota4) / 4
    alunos.append(aluno)
    medias.append(media)

    if media >=7.0:
        aprovados += 1

print(alunos)
print(medias)
print(f"O número total de alunos aprovados foi de {aprovados}!")