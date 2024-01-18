#Exercício 4 - Lista 2

consoante = []
vogal = []
for i in range(10):
    caracteres = input(f"Digite o {i+1}º caracter desejado: ")
    if caracteres not in 'aeiouAEIOU':
        consoante.append(caracteres)
    else:
        vogal.append(caracteres)

print(f'Existe um total de {(len(consoante))} consoantes nos caracteres inseridos.')
print(consoante)