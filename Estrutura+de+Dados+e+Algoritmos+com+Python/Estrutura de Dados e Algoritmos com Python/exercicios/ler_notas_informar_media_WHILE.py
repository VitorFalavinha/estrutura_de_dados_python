nota = int(input('Digite a nota: '))

notaCount = 1
soma = nota
while notaCount < 5:
    soma = soma + nota
    notaCount += 1
    nota = int(input('Digite a nota: '))


media = soma/5
print('A media das notas é: ', media)