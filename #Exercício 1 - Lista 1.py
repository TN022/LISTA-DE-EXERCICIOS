#Exercício 1 - Lista 1

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

a, b = b, a

print(f"Depois da troca, o valor de a é: {a}")
print(f"Depois da troca, o valor de b é: {b}")