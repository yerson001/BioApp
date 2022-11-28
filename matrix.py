import tkinter as tk
import random
AdjustPositionx = 0
AdjustPositiony = -30

root= tk.Tk()

canvas1 = tk.Canvas(root, width=600, height=400, relief='raised')
canvas1.pack()

tittleNW = tk.Label(root, text='Needleman-Wunsch')
tittleNW.config(font=('helvetica', 14))
canvas1.create_window(300, 25, window=tittleNW)

Seq1 = tk.Label(root, text='Secuencia a:')
Seq1.config(font=('helvetica', 10))
canvas1.create_window(100, 100+AdjustPositiony, window=Seq1)

entry1 = tk.Entry(root)
canvas1.create_window(250, 100+AdjustPositiony, window=entry1)

Seq2 = tk.Label(root, text='Secuencia b:')
Seq2.config(font=('helvetica', 10))
canvas1.create_window(100, 150+AdjustPositiony, window=Seq2)

entry2 = tk.Entry(root)
canvas1.create_window(250, 150+AdjustPositiony, window=entry2)



numfont = 0

###############################################################
tittleNW = tk.Label(root, text='Score: ')
tittleNW.config(font=('helvetica', 10+numfont))
canvas1.create_window(90, 250, window=tittleNW)

score = tk.Label(root, text='0 ')
score.config(font=('helvetica', 10+numfont))
canvas1.create_window(90, 270, window=score)



tittleNW = tk.Label(root, text='Num Alig: ')
tittleNW.config(font=('helvetica', 10+numfont))
canvas1.create_window(200, 250, window=tittleNW)

NumAling = tk.Label(root, text='0 ')
NumAling.config(font=('helvetica', 10+numfont))
canvas1.create_window(200, 270, window=NumAling)



tittleNW = tk.Label(root, text='Num Alig: ')
tittleNW.config(font=('helvetica', 10+numfont))
canvas1.create_window(300, 250, window=tittleNW)

Alingmts = tk.Label(root, text=':-)')
Alingmts.config(font=('helvetica', 10+numfont))
canvas1.create_window(300, 270, window=Alingmts)

def fill_divider(n):
    divider = []
    for i in range(len(n)):
        divider.append('|')
        for j in range(len(n[0])):
            divider.append(n[i][j])
        divider.append('|')
    return divider

def random_color():
    colors = ['red2', 'green2', 'gold', 'yellow', 'orange', 'cyan', 'maroon1']
    r = lambda: random.randint(0,len(colors)-1)
    return colors[r()]

def ShowAligments(n,m,space,posx=300,posy=270):
    space_ = space
    pace_ = space
    for i in range(len(n)):
        space_+=space
        rbg = random_color()
        rfg = "black"
        if n[i] == '|':
            rbg = 'blue2'
            rfg = 'blue2'
        ALI = tk.Label(canvas1, text=n[i], bg=rbg, fg=rfg)
        ALI.config(font=('helvetica', 10))
        canvas1.create_window(posx+space_, posy, window=ALI)

        pace_+=space
        ALI = tk.Label(canvas1, text=m[i], bg=rbg, fg=rfg)
        ALI.config(font=('helvetica', 10))
        canvas1.create_window(posx+pace_, posy + 18, window=ALI)

def show_matrix(matrix, seq1, seq2, inx,iny,posx=300, posy=270):
    space_ = 20
    spacey = posy
    spacex = posx
    for i in range(len(seq1)):
        space_ +=20
        ALI = tk.Label(canvas1, text=seq1[i], bg="gray", fg='black')
        ALI.config(font=('helvetica', 10))
        canvas1.create_window(posx+space_, posy-20, window=ALI)
    space_1 =0
    for i in range(len(seq2)):
        space_1 +=20
        ALI = tk.Label(canvas1, text=seq2[i], bg="gray", fg='black')
        ALI.config(font=('helvetica', 10))
        canvas1.create_window(posx+20, posy+space_1-20, window=ALI)

    space_ = 20
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            space_+=20
            rgb = "white"
            if matrix[i] == inx[j] and j == iny[j]:
                rbg = 'yellow'
            ALI = tk.Label(canvas1, text=matrix[i][j], bg=rgb, fg="black")
            ALI.config(font=('helvetica', 10))
            canvas1.create_window(spacex+space_, spacey, window=ALI)
        spacey+=20
        space_ = 20


def get_sequnces():
    seq1 = '-' + "AGC"
    seq2 = '-' + "AAAC" 
    print(len(seq1), len(seq2))


    Score = tk.Label(root, text="3", font=('helvetica', 10, 'bold'))
    canvas1.create_window(85, 270, window=Score)

    NumAling = tk.Label(root, text="gg", font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 270, window=NumAling)

    matrix = [[ 0, -2, -4, -6],
            [-2 , 1, -1, -3],
            [-4, -1 , 0 ,-2],
            [-6, -3, -2, -1],
            [-8 ,-5 ,-4 ,-1]]
    inx = [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0]
    iny = [3, 2, 1, 0, 0, 3, 2, 1, 1, 0, 3, 2, 2, 1, 0]


    ShowAligments(fill_divider(['ABC','KKI']),fill_divider(['AAB','CFD']),20,300,270)
    show_matrix(matrix,seq1, seq2,inx,iny, 400, 150)


button1 = tk.Button(text='Run', command=get_sequnces, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
