from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo = passo * -1
    if passo == 0:
        passo = 1
    print('-='*20)
    print(f'Contando de {inicio} a {fim} de {passo} em {passo}: \n') 

    if inicio < fim: 
        for i in range (inicio, fim+1, passo):
            print(i, end=' ')
            sleep(0.2)
        print('FIM!')
    
    if inicio > fim:
        passo = passo * -1
        for i in range (inicio, fim-1, passo):
            print(i, end=' ')
            sleep(0.2)
        print('FIM!')

    
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez: ')
start = int(input('Inicio: '))
finish = int(input('Fim: '))
passe = int(input('Passo: '))
contador(start, finish, passe)