Descrição

Ambrosiana tem um delivery de frango assado.

O seu problema atual é o gerenciamento da lista de pedidos.

Cada pedido corresponde a um número inteiro  (1 <= PEDIDO <= 10000). 
Os pedidos podem ser cancelados a qualquer momento. 
Além disso, de tempos em tempos, é importante ter a lista de pedidos atualizada em sua mesa. 
Sua missão é ajudar no gerenciamento dos pedidos, considerando que novos pedidos podem ser adicionados à lista assim como podem ser removidos. 
O programa deve encerrar quando a entrada for igual ao caracter s.

Formato de entrada
A entrada consiste de várias linhas, sendo que cada linha pode ser:

    um novo pedido: nesse caso, a linha inicia com a letra a seguida do PEDIDO. 
    Significa que o PEDIDO deve ser adicionado na fila de pedidos.

    cancelamento de um pedido: nesse caso, a linha inicia com a letra r  seguida do PEDIDO. 
    Significa que o PEDIDO deve ser removido da fila. Não existem PEDIDOS duplicados na fila. 
    Se o PEDIDO existir, você deve imprimir "removido", caso contrário imprima "falha".

    impressão da lista de pedidos: nesse caso, a linha inicia com a letra p.  
    Significa que você deve imprimir a lista de pedidos. Nesse caso, imprima todos os números na mesma linha separados por espaços. Depois do último número não existe espaço.

O programa deve parar quando for digitado o caracter s.

Formato de saída
A saída deve ser impressa de acordo com as entradas dadas.

Exemplos de:

Entrada:
a 5
a 3
p
r 3
a 8
p
a 2
r 7
p
s

Saída:
5 3
removido
5 8
falha
5 8 2

-----00-----

Entrada:
p
a 5
p
a 3
r 5
r 3
p
s

Saída:
vazia
5
removido
removido
vazia