#Exercício 7 - Lista 1

numero = int(input("Digite o número a ser dividido: "))

quociente_divisao = numero/3

resto_divisao = numero % 3

if resto_divisao == 0:
    print(f"O quociente é de: {int(quociente_divisao)} E o resto é de: {resto_divisao}")
elif resto_divisao != 0:
    print(f"O quociente é de: {quociente_divisao:.2f} E o resto é de: {resto_divisao}")
else:
    print("Algum erro ocorreu...")
