def calcular_multa(peso_total):
    limite = 100
    valor_multa_por_quilo = 4


    if peso_total > limite:
        excesso = peso_total - limite
        multa = excesso * valor_multa_por_quilo
        return f"Você pescou {peso_total} quilos. Excedeu o limite em {excesso} quilos. Multa: R${multa:.2f}"
    else:
        return f"Você pescou {peso_total} quilos. Está dentro do limite permitido. Não há multa."


peso_total = float(input("Informe o peso total de peixes pescados no dia (em quilos): "))
resultado = calcular_multa(peso_total)
print(resultado)
