def coleta_dimensoes():
    listaDimensoes = []
    while len(listaDimensoes) < 3:
        dimensao = float(input())
        listaDimensoes.append(dimensao)

    return listaDimensoes


def valida_peso(peso):
    while peso <= 0:
        print("Peso invalido!")
        peso = float(input())

    print("Peso valido!")
    return peso


def valida_dimensoes(lista):
    for i in range(0, len(lista)):
        while lista[i] <= 0:
            print("Dimensoes invalidas!")
            lista = coleta_dimensoes()
    print("Dimensoes validas!")
    return lista


def valida_pacote(peso, lista):
    soma = 0
    validar = True

    while validar == True:
        if peso > 500:
            return validar == False
        else:
            if peso <= 100:
                custoPeso = 0.50
            elif peso > 100:
                custoPeso = 0.50 + (peso - 100) // 10/10

        for i in range(0, len(lista)):
            if lista[i] > 28:
                return validar == False
            else:
                soma += lista[i]

        if soma > 52:
            return validar == False
        else:
            if soma <= 22:
                custoDimensoes = 0.20
            else:
                custoDimensoes = 0.20 + (soma - 22) // 2/10

        custoFinal = custoPeso + custoDimensoes
        print("Custo total do envio: R$ {:.2f}".format(custoFinal))
        break


peso = float(input())
pesoValido = valida_peso(peso)

lista = coleta_dimensoes()
dimensoesValidas = valida_dimensoes(lista)

pacote = valida_pacote(pesoValido, dimensoesValidas)
if pacote == False:
    print('Este pacote nao atende os limites para envio no caixa de autoatendimento, dirija-se ao balcao de atendimento para posta-lo!')
