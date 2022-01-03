n, k = input().split(" ")
n = int(n)
k = int(k)

while 1 <= k <= n <= 100:
    lista = []
    lista2 = []
    num = []
    for x in range(1, n + 1):
        matricula, nomes = input().split("-")
        nomes = str(nomes)
        matricula = int(matricula)
        lista.append(nomes)
        lista2.append(nomes)
        num.append(matricula)

    lista.sort()
    escolhido = lista[k - 1]
    mat = lista2.index(escolhido)
    mat_escolhido = num[mat]

    print("Matricula: {}".format(mat_escolhido))
    print("Nome: {}".format(escolhido))
    break
