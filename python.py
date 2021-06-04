import random as r

li = int(input("Ingrese el limite inferior: "))
ls = int(input("Ingrese el limite superior: "))
n = int(input("Ingrese cantidad de numeros en lista: "))
conjunto = [r.randint(0, 20) for _ in range(n)]
# conjunto=[1,2,7,5,9,10,23,6,14,7,11,85,758,15,50,1589]


def listag7(li, ls, conjunto):
    listaconjunto = []
    for i in conjunto:
        if li <= i and i <= ls:
            listaconjunto.append(i)
    return listaconjunto


print(listag7(li, ls, conjunto)
