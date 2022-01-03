Descrição

Imagine que você fora contratado para fazer um programa para uma loja de tintas, com o objetivo de calcular quantas latas de tinta são necessárias para pintar uma determinada área e calcular o preço final da compra.
A loja trabalha com latas de tinta de:

    24 litros, vendidas a R$91,00 cada e,
    5.4 litros, vendidas a R$23,00 cada.

Sabe-se ainda que cada litro de tinta cobre uma superfície de 7 metros quadrados.

Faça um programa que receba o valor da área a ser pintada em metros quadrados, calcule e imprima:
a) A quantidade de latas de tinta e o preço final, considerando apenas latas de 24 litros.
b) A quantidade de latas de tinta e o preço final, considerando apenas latas de 5.4 litros.

c) A quantidade de latas de tinta e o preço final, considerando ambas as latas, de 24 e 5.4 litros.


Observação: O objetivo no item C) não é otimizar o custo nem a quantidade de tinta, apenas comprar o maior número possível de latas de tintas maiores, isto é, o maior número inteiro, e comprar o restante em latas de tinta menores.

Exemplo: Considerando latas de 10 e 3 litros

    se eu precisar de 28 litros de tinta, devo comprar 2 de 10 litros e 3 de 3 litros
    se eu precisar de 51 litros de tinta, devo comprar 5 de 10 litros e 1 de 3 litros
    se eu precisar de 5 litros de tinta, devo comprar 0 de 10 litros e 2 de 3 litros

Formato de entrada

A entrada será um número real positivo não nulo, não deve ser impresso nenhum texto para pedir os dados de entrada.

Formato de saída

A saída deverá ser impressa conforme o exemplo abaixo:

a) 2 lata(s) de 24 litros: R$ 182.00
b) 6 lata(s) de 5.4 litros: R$ 138.00
c) 1 lata(s) de 24 litros e 1 lata(s) de 5.4 litros: R$ 114.00

Com o número de latas impresso como número inteiro e o custo final impresso com duas casas decimais.

Dicas:

    Usem as funções math.ceil(n) e math.floor(n) para arredondar os números para os inteiros acima e abaixo de n, respectivamente.
    Usem o método str.format() para formatar a string e definir o número de casas decimais dos números a serem impressos.


Exemplo:

Entrada
200

Saída
a) 2 lata(s) de 24 litros: R$ 182.00
b) 6 lata(s) de 5.4 litros: R$ 138.00
c) 1 lata(s) de 24 litros e 1 lata(s) de 5.4 litros: R$ 114.00