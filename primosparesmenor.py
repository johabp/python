# numero pares, impares, primos y los menores que 10 cada una sera una liasta
##
v = [1, 3, 5, 7, 90, 120, 17, 19, 29, 67, 53, 61, 3, 1, 2, 5, 6, 7, 8]
pares = []
impares = []
primos = []
menos10 = []
divisibles = []


def primis_lista(v):
    primos = []
    for i in v:
        if i > 1:
            if i == 2 or i == 3:
                primos.append(i)
            if i % 2 == 0 or i % 3 == 0:
                divisibles.append(i)
            else:
                primos.append(i)
    return primos


print(primis_lista(v))
