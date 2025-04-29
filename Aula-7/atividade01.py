def calcular_valores(num):
    dobro = num * 2
    triplo = num * 3
    quadrado = num ** 2
    return dobro, triplo, quadrado


numero = float(input("Digite o valor em cm: "))


dobro, triplo, quadrado = calcular_valores(numero)


print(f"O dobro do número é: {dobro} cm")
print(f"O triplo do número é: {triplo} cm")
print(f"O quadrado do número é: {quadrado} cm²")
