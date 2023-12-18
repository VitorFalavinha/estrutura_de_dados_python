l1 = []

for i in range (5):
    newItem = int(input('Digite o valor: '))
    l1.append(newItem)

soma = 0
for i in range(len(l1)):
    soma += l1[i]

print('A soma dos itens da lista ', l1, 'é ', soma)