dicio = {}

for i in range(3):
    name = str(input('Digite o nome do aluno: '))
    nota = float(input(f'Digite a nota de {name}: '))
    dicio[name] = nota

soma = 0
for nota in dicio.values():
    soma += nota
    print('Media = ', soma/3)