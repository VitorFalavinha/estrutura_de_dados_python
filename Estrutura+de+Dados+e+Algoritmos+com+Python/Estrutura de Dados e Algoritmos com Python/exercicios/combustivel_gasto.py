def ler_valores():
    tempo = float(input('Digite o tempo de viagem: '))
    velocidade = float(input('Digite a velocidade média: '))
    return tempo, velocidade

def distancia(tempo, velocidade):
    return tempo * velocidade

def litrosGastos(distancia):
    return distancia / 12

def resultado(velocidade, tempo, distancia, litros):
    print('Velocidade: ', velocidade)
    print('Tempo: ', tempo)
    print('Distancia: ', distancia)
    print('Litros: ', litros)

t,v = ler_valores()
d = distancia(t, v)
l = litrosGastos(d)
resultado(v, t, d, l)
