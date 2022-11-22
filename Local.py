import numpy as np


class SmithWaterman:
    def __init__(self):
        self.score = 0

    def maximo(self, matriz, i, j, cadena1, cadena2):
        temp = 0
        if cadena1[j] == cadena2[i]:
            temp = 1
        else:
            temp = -1
        m1 = matriz[i - 1][j - 1] + (1 * temp)
        m2 = matriz[i][j - 1] - 2
        m3 = matriz[i - 1][j] - 2
        z = 0
        op = [m1, m2, m3, z]
        return max(op)

    def invertir_cadena(self, cadena):
        return cadena[::-1]

    def seleccionar_cadena2(self, matriz, n, m, cadena2):
        cadena_devuelta_ = []
        indicei_del_maximo = 0
        indicej_del_maximo = 0
        numero_maximo = 0
        for i in range(1, n):
            for j in range(1, m):
                if matriz[i][j] > numero_maximo:
                    numero_maximo = matriz[i][j]
                    indicei_del_maximo = i
                    indicej_del_maximo = j

        while numero_maximo >= 0 and (matriz[indicei_del_maximo][indicej_del_maximo] > matriz[indicei_del_maximo - 1][
            indicej_del_maximo - 1]):
            cadena_devuelta_ += (cadena2[indicei_del_maximo])
            numero_maximo -= 1
            indicei_del_maximo -= 1
            indicej_del_maximo -= 1
        return cadena_devuelta_

    def formar_diagonales(self, matriz, n, m):
        diagonales = []
        for i in range(1, n):
            for j in range(1, m):
                temp_indice = []
                temp_diagonal = []
                if matriz[i][j] != 0:
                    temp_indice.append(i)
                    temp_indice.append(j)
                    temp_diagonal.append(matriz[i][j])
                    tempi = i + 1
                    tempj = j + 1
                    temp_indice = []

                    while (tempi < n and tempj < m and matriz[tempi][tempj] != 0):
                        temp_indice.append(tempi)
                        temp_indice.append(tempj)
                        temp_diagonal.append(matriz[tempi][tempj])
                        temp_indice = []
                        tempi = tempi + 1
                        tempj = tempj + 1
                    diagonales.append(temp_diagonal)
                if matriz[i][j] == 0:
                    continue
        return diagonales

    def get_max_value(self, diagonales):
        tamano_maslargo = 0
        max_mun = 0
        for i in range(len(diagonales)):
            for j in range(len(diagonales[i])):
                if len(diagonales[i]) >= tamano_maslargo:
                    tamano_maslargo = len(diagonales[i])
                if diagonales[i][j] > max_mun:
                    max_mun = diagonales[i][j]
        return max_mun

    def run_matriz(self, n, m, cadena1, cadena2):
        matriz = np.zeros((len(cadena2), len(cadena1)), int)
        for i in range(1, n):
            for j in range(1, m):
                matriz[i][j] = self.maximo(matriz, i, j, cadena1, cadena2)
        return matriz

    def gen_matrix(self, cadena1, cadena2):
        if len(cadena1) > len(cadena2):
            cadena1, cadena2 = cadena2, cadena1
        m, n = len(cadena1), len(cadena2)
        matriz = self.run_matriz(n, m, cadena1, cadena2)

        return n, m, matriz

    def run_SW(self,str1,str2):
        #sw = SmithWaterman()
        n, m, matriz = sw.gen_matrix(str1, str2)
        diagonales = sw.formar_diagonales(matriz, n, m)
        max_mun = sw.get_max_value(diagonales)
        cadena_comun = sw.seleccionar_cadena2(matriz, n, m, str2)
        cadena_comun = sw.invertir_cadena(cadena_comun)
        #print(matriz)
        #print("maximo = ", max_mun)
        #print("cadena = ", cadena_comun)
        return max_mun,cadena_comun



str1 = "-AGCT"
str2 = "-GCA"

sw = SmithWaterman()

n,m = sw.run_SW(str1,str2)

print(n,"  ",m)