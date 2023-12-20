import numpy as np
import pandas as pd


def contar_aprovados(matrix):
    lin = matriz.shape[0]
    col = matriz.shape[1]
    aprovados = reprovados = ausentes = 0

    for i in range(0, lin):
        for j in range(0, col):
            if matriz[i][j] == "442002106":
                matriz[i][j] = ('VITOR FALAVINHA')

    for i in range(0, lin):
        for j in range(0, col):
            if matriz[i][j] == 'APROVADO':
                print(matriz[i])
                aprovados += 1

    print('Quantidade de aprovados: ', aprovados)

    for i in range(0, lin):
        for j in range(0, col):
            if matriz[i][j] == 'REPROVADO':
                print(matriz[i])
                reprovados += 1

    print('Quantidade de reprovados: ', reprovados)
    for i in range(0, lin):
        for j in range(0, col):
            if matriz[i][j] == "AUSENTE":
                print(matriz[i])
                ausentes += 1

    print('Quantidade de ausentes: ', ausentes)


def ordenar(matrix):
    df = pd.DataFrame(matriz)
    df.sort_values([5], inplace=True, ascending=False)
    pd.set_option('display.max_rows', None)
    print(df)


matriz = np.array([[311, 'PROFESSOR II - INGLÊS', 442000020, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442000085, 4, 26, 30, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442000280, 4, 16, 20, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442000432, 4, 25, 29, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442000450, 4, 20, 24, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442000561, 5, 21, 26, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442000581, 3, 18, 21, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442000829, 5, 30, 35, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442001053, 5, 22, 27, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442001122, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442001236, 3, 21, 24, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442001245, 4, 18, 22, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442001258, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442001260, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442001284, 3, 31, 34, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442001813, 3, 12, 15, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442001917, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442001925, 5, 26, 31, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442001975, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442001982, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442002092, 4, 11, 15, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442002106, 5, 28, 33, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442002124, 3, 28, 31, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442002144, 4, 17, 21, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442002228, 4, 17, 21, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442002234, 4, 33, 37, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442002305, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442002343, 2, 17, 19, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442002407, 3, 17, 20, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442002482, 2, 25, 27, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442002502, 3, 28, 31, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442002541, 5, 30, 35, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442002542, 4, 27, 31, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442002606, 3, 30, 33, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442002692, 7, 18, 25, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442002805, 6, 20, 26, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442003051, 4, 32, 36, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442003054, 5, 30, 35, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442003194, 5, 30, 35, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442003492, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442003507, 4, 31, 35, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442003804, 6, 22, 28, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442003853, 5, 26, 31, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442003966, 4, 7, 11, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442004042, 3, 16, 19, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442004043, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442004046, 5, 11, 16, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442004107, 5, 13, 18, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442004216, 1, 23, 24, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442004374, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442004411, 6, 28, 34, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442004431, 3, 10, 13, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442004484, 6, 20, 26, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442004511, 3, 24, 27, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442004602, 4, 18, 22, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442004604, 4, 30, 34, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442004636, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442004740, 4, 17, 21, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442004868, 3, 16, 19, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442004902, 4, 26, 30, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442005010, 4, 30, 34, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442005056, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442005104, 5, 24, 29, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442005136, 2, 24, 26, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442005204, 4, 35, 39, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442005219, 4, 12, 16, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442005231, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442005234, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442005244, 5, 29, 34, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442005259, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442005319, 4, 26, 30, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442005322, 4, 32, 36, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442005330, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442005406, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442005446, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442005480, 4, 20, 24, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442005513, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442005519, 5, 26, 31, 'APROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442005583, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442005655, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442005667, 3, 22, 25, 'REPROVADO'],
                   [311, 'PROFESSOR II - INGLÊS', 442005689, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442005787, 0, 0, 0, 'AUSENTE'],
                   [311, 'PROFESSOR II - INGLÊS', 442005825, 2, 12, 14, 'REPROVADO']])

matrizDissertativa = np.array([[442000085, 311, 'PROFESSOR II - INGLÊS', 61, 68, 0, 43.0, 'REPROVADO'],
                               [442000829, 311, 'PROFESSOR II - INGLÊS', 52, 16, 34, 34.0, 'REPROVADO'],
                               [442001284, 311, 'PROFESSOR II - INGLÊS', 59, 48, 63, 56.7, 'REPROVADO'],
                               [442001925, 311, 'PROFESSOR II - INGLÊS', 79, 83, 58, 73.3, 'APROVADO'],
                               [442002106, 311, 'PROFESSOR II - INGLÊS', 62, 89, 87, 79.3, 'APROVADO'],
                               [442002124, 311, 'PROFESSOR II - INGLÊS', 61.5, 74, 65, 66.8, 'APROVADO'],
                               [442002234, 311, 'PROFESSOR II - INGLÊS', 47, 84, 71, 67.3, 'APROVADO'],
                               [442002502, 311, 'PROFESSOR II - INGLÊS', 77, 52, 66, 65.0, 'APROVADO'],
                               [442002541, 311, 'PROFESSOR II - INGLÊS', 59, 66, 57, 60.7, 'APROVADO'],
                               [442002542, 311, 'PROFESSOR II - INGLÊS', 86, 66, 81, 77.7, 'APROVADO'],
                               [442002606, 311, 'PROFESSOR II - INGLÊS', 90, 81, 73, 81.3, 'APROVADO'],
                               [442003051, 311, 'PROFESSOR II - INGLÊS', 91, 59, 75, 75.0, 'APROVADO'],
                               [442003054, 311, 'PROFESSOR II - INGLÊS', 70, 79, 83, 77.3, 'APROVADO'],
                               [442003194, 311, 'PROFESSOR II - INGLÊS', 87, 61, 66, 71.3, 'APROVADO'],
                               [442003507, 311, 'PROFESSOR II - INGLÊS', 66, 52, 55, 57.7, 'REPROVADO'],
                               [442003853, 311, 'PROFESSOR II - INGLÊS', 64, 49, 54, 55.7, 'REPROVADO'],
                               [442004411, 311, 'PROFESSOR II - INGLÊS', 79, 76, 44, 66.3, 'APROVADO '],
                               [442004604, 311, 'PROFESSOR II - INGLÊS', 55, 76, 70, 67.0, 'APROVADO '],
                               [442004902, 311, 'PROFESSOR II - INGLÊS', 57, 48, 42, 49.0, 'REPROVADO'],
                               [442005010, 311, 'PROFESSOR II - INGLÊS', 84, 79, 43, 68.7, 'APROVADO '],
                               [442005204, 311, 'PROFESSOR II - INGLÊS', 89, 64, 89, 80.7, 'APROVADO '],
                               [442005244, 311, 'PROFESSOR II - INGLÊS', 66, 60, 78, 68.0, 'APROVADO '],
                               [442005319, 311, 'PROFESSOR II - INGLÊS', 73, 0, 0, 24.3, 'REPROVADO '],
                               [442005322, 311, 'PROFESSOR II - INGLÊS', 53, 58, 67, 59.3, 'REPROVADO '],
                               [442005519, 311, 'PROFESSOR II - INGLÊS', 77, 66, 80, 74.3, 'APROVADO']])

#column_names = ["cod", "cargo", "inscricao", "n1", "n2", "n3", "situation"]
#df = pd.DataFrame(matriz, columns=column_names)

#contar_aprovados(matriz)
#somar_notas(matriz, matrizDissertativa)
#ordenar(matriz)
