def contador(n):
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    valores = []
    for indice in range(0, len(notas)):
        while n >= notas[indice]:
            valores.append(notas[indice])
            n -= notas[indice]
            n = round(n, 2)

    for indice in range(0, len(moedas)):
        while n >= moedas[indice]:
            valores.append(moedas[indice])
            n -= moedas[indice]
            n = round(n, 2)

    return valores


n = float(input("Digie um valor: "))
valoresRepetidos = contador(n)
valores = sorted(set(valoresRepetidos), key=float, reverse=True)

for v in range(0, len(valores)):
    valor = valores[v]
    if valor >= 2:
        print("{} nota(s) de R$ {:.2f}".format(
            valoresRepetidos.count(valor), valor))
    else:
        print("{} moeda(s) de R$ {:.2f}".format(
            valoresRepetidos.count(valor), valor))