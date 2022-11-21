import tkinter as tk
from Global import NeedlemanWunsch

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



def get_sequnces():
    seq1 = '-' + entry1.get()
    seq2 = '-' + entry2.get()
    nw = NeedlemanWunsch()
    score_, num, m = nw.run(seq1, seq2)

    Score = tk.Label(root, text=score_, font=('helvetica', 10, 'bold'))
    canvas1.create_window(85, 270, window=Score)

    NumAling = tk.Label(root, text=num, font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 270, window=NumAling)


button1 = tk.Button(text='Run', command=get_sequnces, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()

