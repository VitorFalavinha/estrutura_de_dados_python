m1 = float(input('Digite a primeira nota: '))
m2 = float(input('Digite a segunda nota: '))
m3 = float(input('Digite a terceira nota: '))

media = (m1+m2+m3) / 3

if media <= 4.0:
    print('REPROVADO! Média: ', media)
elif media <= 6.0:
    print('EXAME!')
    nExame = float(input('Digite a nota do exame: '))
    if nExame > 6.0:
        print('APROVADO!')
    else:
        print('REPROVADO!')
else:
    print('APROVADO!')
