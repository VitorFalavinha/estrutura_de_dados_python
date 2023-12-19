def maior(lst):
    print(lst)
    print('Quantidade de itens da lista: ', len(lst))
    maior = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > maior:
            maior = lst[i]
    print('O maior numero da lista é: ', maior)

    
valores = [1, 3, 5, 7]
maior(valores)
