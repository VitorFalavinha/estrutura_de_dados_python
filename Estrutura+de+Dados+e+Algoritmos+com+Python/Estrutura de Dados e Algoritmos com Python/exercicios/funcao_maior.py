from time import sleep

def maior(* num):
    print('-=' * 30)
    cont = maior = 0
    print('Analisando os valores passados...')
    print('Os numeros informados foram: ', end='')
    for valor in num:
        print(f'[{valor}] ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        elif valor > maior: 
            maior = valor
        cont += 1
    print(f'totalizando {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
