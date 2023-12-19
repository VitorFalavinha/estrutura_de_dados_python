from time import sleep

def maior(*num):
    print('-=' * 30)
    print('Analisando os numeros...')
    if (len(num)) == 0:
        print('A sua sequencia não possui numeros.')
    else:
        print(f'Recebi os valores {num}, são ao todo {len(num)}. \nO maior destes numeros é {max(num)}')
    sleep(0.5)
    print()


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()