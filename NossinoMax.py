import numpy as np
import pandas as pd

class nossinov:
    def __init__(self):
        pass

    def couple(self,pair):
        pairs = {"A": "U", "U": "A", "G": "C", "C": "G"}
        if pair in pairs.items():
            return True
        return False

    def fill(self,nm, rna):
 
        minimal_loop_length = 0

        for k in range(1, len(rna)):
            for i in range(len(rna) - k):
                j = i + k

                if j - i >= minimal_loop_length:
                    down = nm[i + 1][j] # 1st rule
                    left = nm[i][j - 1] # 2nd rule
                    diag = nm[i + 1][j - 1] + self.couple((rna[i], rna[j])) # 3rd rule

                    rc = max([nm[i][t] + nm[t + 1][j] for t in range(i, j)]) # 4th rule

                    nm[i][j] = max(down, left, diag, rc) # max of all
                
                else:
                    nm[i][j] = 0

        return nm

    def traceback(self,nm, rna, fold, i, L):

        j = L

        if i < j:
            if nm[i][j] == nm[i + 1][j]: # 1st rule
               self.traceback(nm, rna, fold, i + 1, j)
            elif nm[i][j] == nm[i][j - 1]: # 2nd rule
                self.traceback(nm, rna, fold, i, j - 1)
            elif nm[i][j] == nm[i + 1][j - 1] + self.couple((rna[i], rna[j])): # 3rd rule
                fold.append((i, j))
                self.traceback(nm, rna, fold, i + 1, j - 1)
            else:
                for k in range(i + 1, j - 1):
                    if nm[i][j] == nm[i, k] + nm[k + 1][j]: # 4th rule
                        self.traceback(nm, rna, fold, i, k)
                        self.traceback(nm, rna, fold, k + 1, j)
                        break

        return fold
    def traceback_1(self,nm, rna, fold, i, L):

        j = L

        if i < j:
            if nm[i][j] == nm[i + 1][j]: # 1st rule
               self.traceback(nm, rna, fold, i + 1, j)
               fold.append((i, j))
            elif nm[i][j] == nm[i][j - 1]: # 2nd rule
                self.traceback(nm, rna, fold, i, j - 1)
                fold.append((i, j))
            elif nm[i][j] == nm[i + 1][j - 1] + self.couple((rna[i], rna[j])): # 3rd rule
                fold.append((i, j))
                self.traceback(nm, rna, fold, i + 1, j - 1)
            else:
                for k in range(i + 1, j - 1):
                    if nm[i][j] == nm[i, k] + nm[k + 1][j]: # 4th rule
                        self.traceback(nm, rna, fold, i, k)
                        self.traceback(nm, rna, fold, k + 1, j)
                        fold.append((i, j))
                        break

        return fold

    def dot_write(self,rna, fold):
        dot = ["." for i in range(len(rna))]

        for s in fold:
            #print(min(s), max(s))
            dot[min(s)] = "("
            dot[max(s)] = ")"

        return "".join(dot)

    def init_matrix(self,rna):
        M = len(rna)
        nm = np.empty([M, M])
        nm[:] = np.NAN
        nm[range(M), range(M)] = 0
        nm[range(1, len(rna)), range(len(rna) - 1)] = 0

        return nm

if __name__ == "__main__":
    rna = "GGGAAAUCC"

    a = nossinov()
    nm = a.init_matrix(rna)
    nm = a.fill(nm, rna)
    fold = []
    sec = a.traceback(nm, rna, fold, 0, len(rna) - 1)

    res = a.dot_write(rna, fold)
    names = [_ for _ in rna]
    
    df = pd.DataFrame(nm, index = names, columns = names)	
    
    print(df, "\n", rna, res)
    print(a.traceback_1(nm, rna, fold, 0, len(rna) - 1))
