from random import randint
from time import sleep

def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)

#def somaPar():

numeros = list()
sorteia(numeros)


