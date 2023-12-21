def soma(a, b, c):
    somatorio = a+b+c
    print(somatorio)
    return somatorio


def mult(a, b, c):
    produto = a*b*c
    print(produto)
    return produto


def isPalindromo(string):
    if string == string[::-1]:
        print('É palindromo')
        return True
    else:
        print('Não é palindromo')
        return False


def divisao(a,b):
    print(a/b)
    return a/b


def ler_string(mensagem):

    return input(mensagem)


def ler_float(num):
    return float(input(num))

