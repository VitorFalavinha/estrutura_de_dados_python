def escreva(mensagem):
    tam = len(mensagem) + 4
    print(tam * '~')
    print(f'{mensagem.center(tam)}')
    print(tam * '~')

mens = input('Digite a mensagem: ')
escreva(mens)