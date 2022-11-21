import numpy as np
import time
import graphviz
import networkx as nx

h = graphviz.Digraph('H', filename='hello.gv')
G = nx.DiGraph()


class NeedlemanWunsch:
    def __init__(self):
        self.score = 0

    def swap_(self, str1, str2):
        temp = str1
        str1 = str2
        str2 = temp
        return str1, str2

    def fill_(self, m, n):
        matrix = np.zeros((n, m), int)
        lleno = 0
        # fila de la cadena mas larga
        for i in range(0, n):
            matrix[i][0] = lleno
            lleno += -2
        lleno = 0
        # columna de la cadena mas larga
        for i in range(0, m):
            matrix[0][i] = lleno
            lleno += -2
        return matrix

    def maximo(self, matriz, i, j, str1, str2):
        lista_valores = []
        lista_temp = []
        lista_temp2 = []
        lista_temp3 = []
        alin = 0
        # alineamiento = or  !=

        if str1[j] == str2[i]:
            alin = 1
        else:
            alin = -1
        M1 = matriz[i - 1][j - 1] + (1 * alin)
        M2 = matriz[i][j - 1] - 2
        M3 = matriz[i - 1][j] - 2
        numeros = [M1, M2, M3]

        if M1 == M3 == M2 and M1 == max(numeros):
            lista_temp.append(i - 1)
            lista_temp.append(j - 1)
            lista_valores.append(lista_temp)
            lista_temp2.append(i)
            lista_temp2.append(j - 1)
            lista_valores.append(lista_temp2)
            lista_temp3.append(i - 1)
            lista_temp3.append(j)
            lista_valores.append(lista_temp3)

        elif M1 == M2 and M1 == max(numeros):
            lista_temp.append(i - 1)
            lista_temp.append(j - 1)
            lista_valores.append(lista_temp)
            lista_temp2.append(i)
            lista_temp2.append(j - 1)
            lista_valores.append(lista_temp2)

        elif M1 == M3 and M1 == max(numeros):
            lista_temp.append(i - 1)
            lista_temp.append(j - 1)
            lista_valores.append(lista_temp)
            lista_temp3.append(i - 1)
            lista_temp3.append(j)
            lista_valores.append(lista_temp3)

        elif M2 == M3 and M2 == max(numeros):
            lista_temp2.append(i)
            lista_temp2.append(j - 1)
            lista_valores.append(lista_temp2)
            lista_temp3.append(i - 1)
            lista_temp3.append(j)
            lista_valores.append(lista_temp3)

        elif M1 == max(numeros):
            lista_temp.append(i - 1)
            lista_temp.append(j - 1)
            lista_valores.append(lista_temp)

        elif M2 == max(numeros):
            lista_temp.append(i)
            lista_temp.append(j - 1)
            lista_valores.append(lista_temp)

        elif M3 == max(numeros):
            lista_temp2.append(i - 1)
            lista_temp2.append(j)
            lista_valores.append(lista_temp2)
        return max(numeros), lista_valores

    def convert(self, list):
        return tuple(i for i in list)

    def recorrer_matrix(self, matrix, x, y):
        if (x == 0 and y != 0):
            G.add_edge((x, y), (x, y - 1), weight=-1)
            self.recorrer_matrix(matrix, x, y - 1)
        if (y == 0 and x != 0):
            G.add_edge((x, y), (x - 1, y), weight=-1)
            self.recorrer_matrix(matrix, x - 1, y)
        if (x == 0 and y == 0 or (x - 1 < 0 or y - 1 < 0)):
            return 0
        tam = len(matrix[x - 1][y - 1])
        for i in range(1, tam):
            self.recorrer_matrix(matrix, matrix[x - 1][y - 1][i][0], matrix[x - 1][y - 1][i][1])
            # print(" ",matrix[x-1][y-1][i][0],"  ",matrix[x-1][y-1][i][1])
            G.add_edge((x, y), self.convert(matrix[x - 1][y - 1][i]), weight=1)

    def alineamiento(self, matrix):
        tam_x = len(matrix)
        tam_y = len(matrix[0])
        # print("-----tamaño matriz------")
        # print(tam_x,"  ",tam_y)
        self.recorrer_matrix(matrix, tam_x, tam_y)

    def alineamientos(self, lista_cam, lista2, str2, str1):
        # print("Lista de Caminos:", lista_cam)
        # print("lista2:", lista2)
        cadena_temp = str1[1:]
        lista_temp = ''
        temp_indice = len(cadena_temp) - 1
        for i in range(0, len(lista_cam)):
            for j in range(0, len(lista_cam[0]) - 1):
                if (lista_cam[i][j] == lista_cam[i][j + 1] + 1 or lista_cam[i][j] == lista_cam[i][j + 1] - 1):
                    lista_temp += cadena_temp[temp_indice]
                    temp_indice -= 1

                else:
                    lista_temp += '-'

            lista2.append(lista_temp[::-1])
            # lista2.append("|")
            temp_indice = len(cadena_temp) - 1
            lista_temp = ''
        # print("lista2 Final:", lista2)
        return lista2

    def follow_path(self, lista_caminos, m, n):
        temp = []
        self.alineamiento(lista_caminos)
        # print(lista_caminos)
        # fechas desde [0][0] -> mtx[m-1][n-1]
        lista = [e for e in G.edges]
        # print(lista)
        # fechas desde mtx[m-1][n-1] -> [0][0]
        lista2 = [i for i in reversed(lista)]
        val_ini = lista2[0][0]
        for path in nx.all_simple_paths(G, source=(n - 1, m - 1), target=(0, 0)):
            temp.append(path)
        return temp

    def get_alignments(self, lista_graph, matriz):
        lista_alineamientos = []
        for i in range(len(lista_graph)):
            # lista_alineamientos_temp1 = []
            lista_alineamientos_temp = []
            for j in range(len(lista_graph[0])):
                tup1 = lista_graph[i][j]
                indicei = tup1[0]
                indicej = tup1[1]
                # obtenemos el valor indice = M[i][j]
                indice = matriz[indicei][indicej]
                lista_alineamientos_temp.append(indice)
            lista_alineamientos.append(lista_alineamientos_temp)
        return lista_alineamientos

    def run(self, str1, str2):
        lista_caminos = []
        if len(str2) < len(str1):
            str1, str2 = self.swap_(str1, str2)
        m, n = len(str1), len(str2)
        matriz = self.fill_(m, n)

        for i in range(1, n):
            lista_temp4 = []
            for j in range(1, m):
                lista_temp = []
                lista_temp2 = []
                lista_temp3 = []
                # ---------------------------
                # 3. maximos valores
                # ---------------------------
                matriz[i][j], lista_temp = self.maximo(matriz, i, j, str1, str2)
                lista_temp3.append(matriz[i][j])
                lista_temp3 += (lista_temp)
                lista_temp4.append(lista_temp3)

            lista_caminos.append(lista_temp4)
        # #----------------------------------------
        lista_graph = self.follow_path(lista_caminos, m, n)
        lista_alineamientos = self.get_alignments(lista_graph, matriz)
        alignments = []
        lista2 = []
        cadena_temp = str2[1:]
        for i in range(0, len(lista_alineamientos)):
            alignments.append(cadena_temp)
        score = matriz[n - 1][m - 1]
        letters = self.alineamientos(lista_alineamientos, lista2, str2, str1)
        """
        print("MATRIZ: ")
        print(matriz)
        print("SCORE : ", score)
        print("ALINEAMIENTOS # : ", len(lista_alineamientos))
        print("ALINEAMIENTOS ", lista_alineamientos)
        print(alignments)
        print(letters)
        """
        return score,len(lista_alineamientos),lista_caminos


if __name__ == '__main__':
    seq1 = '-' + 'AGC'
    seq2 = '-' + 'AAAC'
    nw = NeedlemanWunsch()
    score,num,m = nw.run(seq1, seq2)

    print(score, " \n ",num, " \n ",m)





