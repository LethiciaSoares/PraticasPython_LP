Descrição

Tia Joana é uma respeitada professora e tem vários alunos. 
Em sua última aula, ela prometeu que iria sortear um aluno para ganhar um bônus especial na nota final: 
ela colocou N pedaços de papel numerados de 1 a N em um saquinho e sorteou um determinado número K; 
o aluno premiado foi o K-ésimo aluno na lista de chamada do diário de classe, a qual contém os nomes em ordem alfabética.

O problema é que a Tia Joana esqueceu o diário de classe, então ela não tem como saber quem é o K-ésimo aluno na lista de presença. 
Porém, os alunos dela estão muito ansiosos e querem logo saber quem foi o vencedor. Por isso eles decidiram fazer um programa de computador para ler os dados de suas carteiras de estudante 
(nome e matrícula) e colocar todos os alunos em ordem alfabética. 
Desta forma eles poderiamdescobrir quem é o K-ésimo aluno na lista, isto é, quem foi o ganhador.

Portanto, seu trabalho é criar um programa de computador, que a partir das matrículas e nomes dos alunos da Tia Joana e do número sorteado, 
determine a matrícula e o nome do aluno que deve receber o bônus.


Formato de entrada
A primeira linha contém dois inteiros N e K separados por um espaço em branco (1 ≤ K ≤ N ≤ 100). 
Cada uma das N linhas seguintes contém uma matrícula (até 6 dígitos) e uma cadeia de caracteres de tamanho mínimo 1 e máximo 20 representando os nomes dos alunos. 
Os nomes são compostos apenas por letras minúsculas de 'a' a 'z'.

Formato de saída
Seu programa deve imprimir duas linhas, a primeira contendo o número de matrícula e outra o nome do aluno, seguindo a formatação contida no exemplo.

+--Entrada -------------Saída Esperada----+
|                 |                       |
|    5 1          |     Matricula: 33333  |
|   11111-maria   |     Nome: carlos      |
|   22222-joao    |                       |
|   33333-carlos  |                       |
|   44444-vanessa |                       |
|   55555-jose    |                       |
+-----------------------------------------+
