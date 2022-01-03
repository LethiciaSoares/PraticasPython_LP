salario = float(input())

aliquota1 = 0.08
aliquota2 = 0.09
aliquota3 = 0.11


def calculo_contribuicao1():
    contr = salario*aliquota1
    print("Desconto do INSS: R$ {:.2f}".format(contr))


def calculo_contribuicao2():
    contr = salario*aliquota2
    print("Desconto do INSS: R$ {:.2f}".format(contr))


def calculo_contribuicao3():
    contr = salario*aliquota3
    print("Desconto do INSS: R$ {:.2f}".format(contr))


def calculo_contribuicao_teto():
    contr = 5839.45*aliquota3
    print("Desconto do INSS: R$ {:.2f}".format(contr))


if salario <= 1751.81:
    calculo_contribuicao1()
elif salario > 1751.81 and salario <= 2919.72:
    calculo_contribuicao2()
elif salario > 2919.72 and salario <= 5839.45:
    calculo_contribuicao3()
else:
    calculo_contribuicao_teto()