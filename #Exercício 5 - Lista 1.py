#Exercício 5 - Lista 1

notas = [200, 100, 50 , 20, 10, 5, 2 , 1, 0.50, 0.25, 0.10, 0.05]

valor_da_compra = float(input("Digite o valor total da compra: "))

valor_pago = float(input("Digite o valor que foi pago para receber o troco: "))

troco = valor_pago - valor_da_compra

print("Troco a ser dado:")

for nota in notas:
    if troco >= nota:
        quantidade = int(troco / nota)
        troco -= quantidade * nota
        if nota>1:
            print(f"{quantidade} nota(s) de R${nota:.2f}")
        else:
            print(f"{quantidade} moeda(s) de R${nota:.2f}")