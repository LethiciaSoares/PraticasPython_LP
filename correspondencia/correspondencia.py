from math import floor

def media_carta():
    media = (sum(lista)/len(lista))
    print(floor(media))


lista = []
meta = []
for x in range(1, 8):
    cartas = int(input())
    lista.append(cartas)
    if cartas >= 100:
        meta.append(cartas)

cumpriu = len(meta)
print(cumpriu)
media_carta()
