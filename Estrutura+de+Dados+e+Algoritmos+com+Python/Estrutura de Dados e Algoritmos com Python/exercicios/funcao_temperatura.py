def ler_temperatura():
    temperatura = float(input('Digite a temperatura: '))
    return temperatura

def calculo(temperatura_celsius): 
    temperatura_f = (9 * temperatura_celsius + 160)/5
    return temperatura_f

def resultado(temperatura_f):
    print(f'{temperatura_c} graus celsius é igual a {temperatura_f} graus Farenheit. ') 


temperatura_c = ler_temperatura()
temperatura_f = calculo(temperatura_c)
resultado(temperatura_f)