lista = []
try:
    lista.append(float(input('Digite o primeiro valor: ')))
    lista.append(float(input('Digite o segundo valor: ')))
    divisao = lista[0] / lista[1]
    print(lista)

except ValueError:
    print('Erro! Valor inválido.')
except ZeroDivisionError:
    print('Erro! Divisao por zero.')
except IndexError:
    print('Erro! Indice inválido.')
except KeyboardInterrupt:
    print('Usuario interompeu a excução.')
else:
    print(f'A divisao de {lista[0]} e {lista[1]} é {divisao}.')