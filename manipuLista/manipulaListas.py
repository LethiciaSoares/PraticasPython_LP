fim = True
listaPedido = []

while fim:
    pedido = input().split(" ")

    if pedido[0] == "a":
        pedidoInt = int(pedido[1])
        if not pedidoInt in listaPedido:
            listaPedido.append(pedidoInt)
        else:
            print("falha")

    elif pedido[0] == "r":
        pedidoInt = int(pedido[1])
        if not pedidoInt in listaPedido:
            print("falha") 
        else:
            listaPedido.remove(pedidoInt)
            print("removido")

    elif pedido[0] == "p":
        if len(listaPedido) == 0:
            print('vazia')
        else:
            print(*listaPedido, sep=' ')

    if pedido[0] == "s":
        fim = False