Descrição

Leia um valor de ponto flutuante com duas casas decimais, 
que representa um valor em dinheiro. 
A seguir, calcule o menor número de notas e moedas no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
A seguir mostre a relação de notas necessárias.

Formato de entrada

A entrada será um valor em ponto flutuante N, com 0 < N ≤ 1000000.00. 
(Não é necessário validar)

Formato de saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, 
conforme exemplos dados. Note que são impressas apenas as linhas cujo número de notas 
ou moedas é diferente de zero.

DICA: Se o seu programa calcula errado o número das moedas menores, pense em trabalhar os valores mudando a unidade, assim não precisamos lidar com números decimais. É o que fazemos na prática, falando em números inteiros tanto pros reais quanto pros centavos.

Exemplos de:

Entrada
368.95

Saída
3 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
1 nota(s) de R$ 2.00
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
1 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10

-----00-----

Entrada
2561.47

Saída
25 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 10.00
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
2 moeda(s) de R$ 0.01

-----00-----

Entrada
576.73

Saída
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
1 nota(s) de R$ 5.00
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
2 moeda(s) de R$ 0.10
3 moeda(s) de R$ 0.01

-----00------

Entrada
4

Saída
2 nota(s) de R$ 2.00