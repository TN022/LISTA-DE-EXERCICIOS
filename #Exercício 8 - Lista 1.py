#Exercício 8 - Lista 1

valor_inicial = float(input("Digite o valor inicial do investimento: "))
juros_anual = float(input("Digite o valor da taxa anual de juros(em porcentagem %): "))
anos_de_investimento = int(input("Digite quantos anos de investimento: "))

juros_decimal = juros_anual/100

montante_final = (valor_inicial * (1 + juros_decimal))**anos_de_investimento

print(f"O montante final após {anos_de_investimento} anos será de R$: {montante_final}")
