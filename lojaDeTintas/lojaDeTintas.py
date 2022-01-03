import math

area = float(input())
pintura = area / 7

a = pintura / 24
b = pintura / 5.4
a1 = math.floor(a)
b1 = math.ceil((area-(a1*7*24))/7/5.4)

print('a)', math.ceil(a), 'lata(s) de 24 litros: R$ %5.2f' % (math.ceil(a) * 91))
print('b)', math.ceil(b), 'lata(s) de 5.4 litros: R$ %5.2f' % (math.ceil(b) * 23))
print('c)', a1, 'lata(s) de 24 litros e', b1, 'lata(s) de 5.4 litros: R$ %5.2f' % (b1 * 23 + a1 * 91))


