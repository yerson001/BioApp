import numpy as np
import time


class startAlingment:
    def __init__(self):
        pass

    def run_matrix(self, x, y, s_match, s_mismatch, s_gap):
        A = []
        for i in range(len(y) + 1):
            A.append([0] * (len(x) + 1))
        for i in range(len(y) + 1):
            A[i][0] = s_gap * i
        for i in range(len(x) + 1):
            A[0][i] = s_gap * i
        for i in range(1, len(y) + 1):
            for j in range(1, len(x) + 1):
                A[i][j] = max(
                    A[i][j - 1] + s_gap,
                    A[i - 1][j] + s_gap,
                    A[i - 1][j - 1] + (s_match if (y[i - 1] == x[j - 1] and y[i - 1] != '-') else 0) + (
                        s_mismatch if (y[i - 1] != x[j - 1] and y[i - 1] != '-' and x[j - 1] != '-') else 0) + (
                        s_gap if (y[i - 1] == '-' or x[j - 1] == '-') else 0)
                )
        align_X = ""
        align_Y = ""
        i = len(x)
        j = len(y)
        while i > 0 or j > 0:
            current_score = A[j][i]
            if i > 0 and j > 0 and (
                    ((x[i - 1] == y[j - 1] and y[j - 1] != '-') and current_score == A[j - 1][i - 1] + s_match) or
                    ((y[j - 1] != x[i - 1] and y[j - 1] != '-' and x[i - 1] != '-') and current_score == A[j - 1][
                        i - 1] + s_mismatch) or
                    ((y[j - 1] == '-' or x[i - 1] == '-') and current_score == A[j - 1][i - 1] + s_gap)
            ):
                align_X = x[i - 1] + align_X
                align_Y = y[j - 1] + align_Y
                i = i - 1
                j = j - 1
            elif i > 0 and (current_score == A[j][i - 1] + s_gap):
                align_X = x[i - 1] + align_X
                align_Y = "-" + align_Y
                i = i - 1
            else:
                align_X = "-" + align_X
                align_Y = y[j - 1] + align_Y
                j = j - 1
        return (align_X, align_Y, A[len(y)][len(x)])

    def get_input(self):
        sequences = []
        n = int(input())
        for i in range(n):
            sequences.append(input())
        return sequences

    def get_center(self, sequences):
        score_matrix = {}
        for i in range(len(sequences)):
            score_matrix[i] = {}
        for i in range(len(sequences)):
            for j in range(len(sequences)):
                if i != j:
                    score_matrix[i][j] = self.run_matrix(sequences[i], sequences[j], 3, -1, -2)
                    # print(score_matrix[i][j][1])
        #     print(score_matrix)

        center = 0
        center_score = float('-inf')
        for scores in score_matrix:
            sum = 0
            for i in score_matrix[scores]:
                #             print(i)
                sum += score_matrix[scores][i][2]
            if sum > center_score:
                center_score = sum
                center = scores
        # print("center",score_matrix[center][2][2])

        # max_ = score_matrix[center][2][2]
        max_ = 0
        alignments_needed = {}
        #     print(score_matrix[center])
        for i in range(len(sequences)):
            # print(i)
            if i != center:
                s1, s2, sc = self.run_matrix(sequences[i], sequences[center], 3, -1, -2)
                alignments_needed[i] = (s2, s1, sc)
        #     print("escore matrix")
        # print(score_matrix)
        # print(alignments_needed)
        return center, alignments_needed, max_

    def align_gaps(self, seq1, seq2, aligneds, new):
        i = 0
        while i < max(len(seq1), len(seq2)):
            try:
                if i > len(seq1) - 1:
                    seq1 = seq1[:i] + "-" + seq1[i:]
                    naligneds = []
                    for seq in aligneds:
                        naligneds.append(seq[:i] + "-" + seq[i:])
                    aligneds = naligneds
                elif i > len(seq2) - 1:
                    seq2 = seq2[:i] + "-" + seq2[i:]
                    new = new[:i] + "-" + new[i:]
                elif (seq1[i] == "-" and i >= len(seq2)) or (seq1[i] == "-" and seq2[i] != "-"):
                    seq2 = seq2[:i] + "-" + seq2[i:]
                    new = new[:i] + "-" + new[i:]
                elif (seq2[i] == "-" and i >= len(seq1)) or (seq2[i] == "-" and seq1[i] != "-"):
                    # print("me")
                    seq1 = seq1[:i] + "-" + seq1[i:]
                    naligneds = []
                    for seq in aligneds:
                        naligneds.append(seq[:i] + "-" + seq[i:])
                    aligneds = naligneds

            except:
                print("salir")
            i += 1

        aligneds.append(new)
        # print(aligneds)
        return seq1, aligneds

    def msa(self, alignments):
        aligned_center = alignments[list(alignments.keys())[0]][0]
        aligneds = []
        aligneds.append(alignments[list(alignments.keys())[0]][1])

        for seq in list(alignments.keys())[1:]:
            cent = alignments[seq][0]
            newseq = alignments[seq][1]
            aligned_center, aligneds = self.align_gaps(aligned_center, cent, aligneds, newseq)

        return aligneds, aligned_center

    def calculate_scores(self, alignments):
        score = 0
        for i in range(len(alignments[0])):
            for j in range(len(alignments) - 1):
                for k in range(j + 1, len(alignments)):
                    if alignments[j][i] == alignments[k][i]:
                        if alignments[j][i] != "-":
                            score += 3

                    elif alignments[k][i] == "-" or alignments[j][i] == "-":
                        score -= 2
                    else:
                        score -= 1
        return score

    def order_results(self, aligneds, center_seq, center):
        i = 0
        j = 0
        results = []
        while i < len(sequences):
            if i == center:
                results.append(center_seq)
                i += 1
            else:
                results.append(aligneds[j])
                i += 1
                j += 1
        return results

    def block_optimization(self, results, score):
        continue_bit = True

        while continue_bit:
            # print(results)
            block_columns = []
            blocks = []
            for i in range(len(results[0])):
                for seq in range(len(results) - 1):
                    if (results[seq][i] != results[seq + 1][i]) or results[seq][i] == "-":
                        block_columns.append(i)
                        break
            i = 0
            while i < len(block_columns):
                col = block_columns[i]
                counter = col
                while counter < len(results[0]):
                    if counter + 1 in block_columns:
                        counter += 1
                    else:
                        break
                if counter != col:
                    blocks.append((col, counter))
                    i = counter
                else:
                    i += 1
            # print(results)

            seq_blocks = []
            for b in blocks:
                block = []
                for seq in results:
                    nseq = seq[b[0]:b[1] + 1]
                    block.append(nseq.replace("-", ""))
                if "" not in block:
                    seq_blocks.append(block)
            # print(seq_blocks)
            block = seq_blocks[0]
            counter = 0
            for block in seq_blocks:

                center, alignments, aa = self.get_center(block)
                aligneds, center_seq = self.msa(alignments)
                # print(block)
                # print(aligneds)
                # print(alignments)
                res = self.order_results(aligneds, center_seq, center)

                index = seq_blocks.index(block)
                # print(res)
                news = []
                for i in range(len(results)):
                    news.append(results[i][:blocks[index][0]] + res[i] + results[i][blocks[index][1] + 1:])

                if self.calculate_scores(news) > score:
                    results = news
                    break
                counter += 1

            if counter == len(seq_blocks):
                continue_bit = False

        return results, self.calculate_scores(results)

    def swap_(self, str1, str2):
        temp = str1
        str1 = str2
        str2 = temp
        return str1, str2

    def fill_(self, str1, str2, m, n):
        m, n = len(str1), len(str2)
        matriz = np.zeros((len(str2), len(str1)), int)
        lleno = 0
        for i in range(0, n):
            matriz[i][0] = lleno
            lleno = lleno - 2

        lleno = 0
        for j in range(0, m):
            matriz[0][j] = lleno
            lleno = lleno - 2
        return matriz

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

    def get_score(self, str1, str2):
        str1 = "-" + str1
        str2 = "-" + str2
        if len(str2) < len(str1):
            str1, str2 = self.swap_(str1, str2)

        m, n = len(str1), len(str2)
        matriz = self.fill_(str1, str2, m, n)

        for i in range(1, n):
            for j in range(1, m):
                lista_temp = []
                matriz[i][j], lista_temp = self.maximo(matriz, i, j, str1, str2)
        score = matriz[n - 1][m - 1]
        return score

    def get_score_matriz(self, sequence):
        matriz = np.zeros((len(sequence), len(sequence)), int)
        for i in range(0, len(sequence)):
            for j in range(0, len(sequence)):
                if i == j:
                    matriz[i][j] = 0
                else:
                    matriz[i][j] = self.get_score(sequence[i], sequence[j])
        return matriz

    def save(matriz, score_, result, str_):

        np.savetxt('save.txt', matriz, fmt='%.0f')
        file1 = open("save.txt", "a")
        file1.write("\n")
        file1.writelines("S" + str(score_ + 1) + ": " + str(str_))
        file1.write(" \n")
        file1.write(" \n")
        for i in (result):
            file1.writelines(str(i))
            file1.write("\n")
        file1.write(" ")
        file1.write(" \n")
        file1.close()

    def run_start(self):
        print("number of sequences: ")
        sequences = self.get_input()
        matriz = self.get_score_matriz(sequences)
        center, alignments, max_ = self.get_center(sequences)
        aligneds, center_seq = self.msa(alignments)
        results = self.order_results(aligneds, center_seq, center)
        print(self.calculate_scores(results))
        results, score = a.block_optimization(results, self.calculate_scores(results))

        print(a.get_score_matriz(sequences))
        print(score)
        print("center --> S" + str(center + 1), ": ", sequences[center])

        print("-------result-----")
        for i in results:
            print(i)


import time

if __name__ == '__main__':

    a = startAlingment()

    str = "ACG,GCA,ACC"

    print("number of sequences: ")
    sequences = a.get_input()
    matriz = a.get_score_matriz(sequences)
    center, alignments, max_ = a.get_center(sequences)
    aligneds, center_seq = a.msa(alignments)
    results = a.order_results(aligneds, center_seq, center)
    print(a.calculate_scores(results))
    results, score = a.block_optimization(results, a.calculate_scores(results))

    print(a.get_score_matriz(sequences))
    print(score)
    print("center --> S" + str(center + 1), ": ", sequences[center])

    print("-------result-----")
    for i in results:
        print(i)
