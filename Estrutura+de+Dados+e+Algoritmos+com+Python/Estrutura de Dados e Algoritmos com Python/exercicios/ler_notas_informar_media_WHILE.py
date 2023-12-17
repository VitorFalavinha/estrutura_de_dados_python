notaCount = 1
soma = 0
while notaCount <= 5:
    nota = int(input('Digite a nota: '))
    soma = soma + nota
    notaCount += 1
    
print('A media das notas é: ', soma/5)