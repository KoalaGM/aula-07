# Funções em python inicia com a palavra
# reservada def.
# Funções são rotinas em seu conceito
# São blocos de códigos que só serão executados se forem chamados.


# def saudacao():
#     print('Olá mundo!')


# saudacao()


def somar_numeros(x, y):
    s = x + y
    # print(soma)
    return s


for i in range(3):
    n1 = int(input('Informe o número: '))
    n2 = int(input('Informe o número: '))

    soma = somar_numeros(n1, n2)
    print(soma)
