idade = int(input('Digite sua idade: '))
if idade < 0:
    print('Idade inválida!!!')
elif idade <= 12:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
else:
    print('Adulto')