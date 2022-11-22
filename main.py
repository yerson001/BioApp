import tkinter as tk
from tkinter import ttk
import re
from Global import NeedlemanWunsch
from Local import SmithWaterman
from Estrella import startAlingment

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._mainCanvas = None
        self._allCanvases = dict()
        self.switch_Canvas(StartUpPage)

    def switch_Canvas(self, Canvas_class):

        if self._mainCanvas:
            self._mainCanvas.pack_forget()
        canvas = self._allCanvases.get(Canvas_class, False)

        if not canvas:
            canvas = Canvas_class(self)
            self._allCanvases[Canvas_class] = canvas

        canvas.pack(pady=60)
        self._mainCanvas = canvas


class StartUpPage(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        # Define the size of the window
        tk.Canvas.__init__(self, master, *args, **kwargs)
        tk.Frame(self, relief="sunken",
                 borderwidth=2)  # Here the parent of the frame is the self instance of type tk.Canvas
        tk.Label(self, text="Algoritmos de Alineamiento de Secuencias").grid(
            column=0, row=0)
        tk.Button(self, text="Neddleman-Wunch",
                  command=lambda: master.switch_Canvas(PageOne)).grid(column=0, row=1)
        tk.Button(self, text="Smith-Waterman",
                  command=lambda: master.switch_Canvas(PageTwo)).grid(column=0, row=2)
        tk.Button(self, text="Satart-Aligment",
                  command=lambda: master.switch_Canvas(PageThree)).grid(column=0, row=3)


class PageOne(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=600, height=400)

        AdjustPositionx = 0
        AdjustPositiony = -30

        tittleNW = tk.Label(self, text='Needleman-Wunsch')
        tittleNW.config(font=('helvetica', 14))
        self.canvas.create_window(300, 25, window=tittleNW)

        Seq1 = tk.Label(self, text='Secuencia a:')
        Seq1.config(font=('helvetica', 10))
        self.canvas.create_window(100, 100 + AdjustPositiony, window=Seq1)

        entry1 = tk.Entry(self)
        self.canvas.create_window(250, 100 + AdjustPositiony, window=entry1)

        Seq2 = tk.Label(self, text='Secuencia b:')
        Seq2.config(font=('helvetica', 10))
        self.canvas.create_window(100, 150 + AdjustPositiony, window=Seq2)

        entry2 = tk.Entry(self)
        self.canvas.create_window(250, 150 + AdjustPositiony, window=entry2)

        numfont = 0

        ###############################################################
        tittleNW = tk.Label(self, text='Score: ')
        tittleNW.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(90, 250, window=tittleNW)

        score = tk.Label(self, text='0 ')
        score.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(90, 270, window=score)

        tittleNW = tk.Label(self, text='Num Alig: ')
        tittleNW.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(200, 250, window=tittleNW)

        NumAling = tk.Label(self, text='0 ')
        NumAling.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(200, 270, window=NumAling)

        tittleNW = tk.Label(self, text='Num Alig: ')
        tittleNW.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(300, 250, window=tittleNW)

        Alingmts = tk.Label(self, text=':-)')
        Alingmts.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(300, 270, window=Alingmts)

        def show_aligments():
            ALI = tk.Label(self, text='A', bg="gray51", fg="red")
            ALI.config(font=('helvetica', 10))
            self.canvas.create_window(400, 270, window=ALI)

            ALI = tk.Label(self, text='A', bg="gray51", fg="blue")
            ALI.config(font=('helvetica', 10))
            self.canvas.create_window(420, 270, window=ALI)

            ALI = tk.Label(self, text='A', bg="gray51", fg="green")
            ALI.config(font=('helvetica', 10))
            self.canvas.create_window(440, 270, window=ALI)

            ALI = tk.Label(self, text='C', bg="gray51", fg="orange")
            ALI.config(font=('helvetica', 10))
            self.canvas.create_window(460, 270, window=ALI)

            ALI = tk.Label(self, text='A', bg="gray51", fg="red")
            ALI.config(font=('helvetica', 10))
            self.canvas.create_window(400, 300, window=ALI)

            ALI = tk.Label(self, text='-', bg="gray51", fg="blue")
            ALI.config(font=('helvetica', 10))
            self.canvas.create_window(420, 300, window=ALI)

            ALI = tk.Label(self, text='G', bg="gray51", fg="green")
            ALI.config(font=('helvetica', 10))
            self.canvas.create_window(440, 300, window=ALI)

            ALI = tk.Label(self, text='C', bg="gray51", fg="orange")
            ALI.config(font=('helvetica', 10))
            self.canvas.create_window(460, 300, window=ALI)

        def get_sequnces():
            seq1 = '-' + entry1.get()
            seq2 = '-' + entry2.get()
            nw = NeedlemanWunsch()
            score_, num, n, m = nw.run(seq1, seq2)

            Score = tk.Label(self, text=score_, font=('helvetica', 10, 'bold'))
            self.canvas.create_window(85, 270, window=Score)

            NumAling = tk.Label(self, text=num, font=('helvetica', 10, 'bold'))
            self.canvas.create_window(200, 270, window=NumAling)

            show_aligments()

        button1 = tk.Button(text='Run', command=get_sequnces,
                            bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        self.canvas.create_window(200, 180, window=button1)

        tk.Label(self, text="First page").pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Back",
                  command=lambda: master.switch_Canvas(StartUpPage)).pack()

        self.canvas.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


class PageTwo(tk.Frame):  # Sub-lcassing tk.Frame
    def __init__(self, master, *args, **kwargs):
        # self is now an istance of tk.Frame
        tk.Frame.__init__(self, master, *args, **kwargs)
        # make a new Canvas whose parent is self.
        self.canvas = tk.Canvas(self, width=600, height=400)

        AdjustPositionx = 0
        AdjustPositiony = -30

        tittleNW = tk.Label(self, text='Smith-Waterman')
        tittleNW.config(font=('helvetica', 14))
        self.canvas.create_window(300, 25, window=tittleNW)

        Seq1 = tk.Label(self, text='Secuencia a:')
        Seq1.config(font=('helvetica', 10))
        self.canvas.create_window(100, 100 + AdjustPositiony, window=Seq1)

        entry1 = tk.Entry(self)
        self.canvas.create_window(250, 100 + AdjustPositiony, window=entry1)

        Seq2 = tk.Label(self, text='Secuencia b:')
        Seq2.config(font=('helvetica', 10))
        self.canvas.create_window(100, 150 + AdjustPositiony, window=Seq2)

        entry2 = tk.Entry(self)
        self.canvas.create_window(250, 150 + AdjustPositiony, window=entry2)

        numfont = 0

        ###############################################################
        tittleNW = tk.Label(self, text='Máximo: ')
        tittleNW.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(90, 250, window=tittleNW)

        score = tk.Label(self, text='0')
        score.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(90, 270, window=score)

        tittleNW = tk.Label(self, text='Num Alig: ')
        tittleNW.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(200, 250, window=tittleNW)

        NumAling = tk.Label(self, text='0 ')
        NumAling.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(200, 270, window=NumAling)

        tittleNW = tk.Label(self, text='ALineacion: ')
        tittleNW.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(300, 250, window=tittleNW)

        Alingmts = tk.Label(self, text=':-)')
        Alingmts.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(300, 270, window=Alingmts)

        def show_alineamientos():
            ALI = tk.Label(self, text='C', bg="gray51", fg="red")
            ALI.config(font=('helvetica', 10))
            self.canvas.create_window(400, 270, window=ALI)

            ALI = tk.Label(self, text='A', bg="gray51", fg="blue")
            ALI.config(font=('helvetica', 10))
            self.canvas.create_window(420, 270, window=ALI)

        def get_sequnces():
            seq1 = '-' + entry1.get()
            seq2 = '-' + entry2.get()

            sw = SmithWaterman()
            m, n = sw.run_SW(seq1, seq2)

            Score = tk.Label(self, text=m, font=('helvetica', 10, 'bold'))
            self.canvas.create_window(85, 270, window=Score)

            NumAling = tk.Label(
                self, text=n[0][0], font=('helvetica', 10, 'bold'))
            self.canvas.create_window(200, 270, window=NumAling)
            show_alineamientos()

        button1 = tk.Button(text='Run', command=get_sequnces,
                            bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        self.canvas.create_window(200, 180, window=button1)

        self.label = tk.Label(self, text="Second page").pack(
            side="top", fill="x", pady=5)
        self.button = tk.Button(
            self, text="Back", command=lambda: master.switch_Canvas(StartUpPage))
        self.button.pack()
        self.canvas.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


class PageThree(tk.Frame):  # Sub-lcassing tk.Frame
    def __init__(self, master, *args, **kwargs):
        # self is now an istance of tk.Frame
        tk.Frame.__init__(self, master, *args, **kwargs)
        # make a new Canvas whose parent is self.
        self.canvas = tk.Canvas(self, width=600, height=400)

        AdjustPositionx = 0
        AdjustPositiony = -30

        tittleNW = tk.Label(self, text='Smith-Waterman')
        tittleNW.config(font=('helvetica', 14))
        self.canvas.create_window(300, 25, window=tittleNW)

        Seq1 = tk.Label(self, text='Secuencia a:')
        Seq1.config(font=('helvetica', 10))
        self.canvas.create_window(100, 100 + AdjustPositiony, window=Seq1)

        entry1 = tk.Entry(self)
        self.canvas.create_window(
            250, 100 + AdjustPositiony, window=entry1)

        Seq2 = tk.Label(self, text='Secuencia b:')
        Seq2.config(font=('helvetica', 10))
        self.canvas.create_window(100, 150 + AdjustPositiony, window=Seq2)

        entry2 = tk.Entry(self)
        self.canvas.create_window(
            250, 150 + AdjustPositiony, window=entry2)

        numfont = 0

        ###############################################################
        tittleNW = tk.Label(self, text='Máximo: ')
        tittleNW.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(90, 250, window=tittleNW)

        score = tk.Label(self, text='0')
        score.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(90, 270, window=score)

        tittleNW = tk.Label(self, text='Num Alig: ')
        tittleNW.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(200, 250, window=tittleNW)

        NumAling = tk.Label(self, text='0 ')
        NumAling.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(200, 270, window=NumAling)

        tittleNW = tk.Label(self, text='ALineacion: ')
        tittleNW.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(300, 250, window=tittleNW)

        Alingmts = tk.Label(self, text=':-)')
        Alingmts.config(font=('helvetica', 10 + numfont))
        self.canvas.create_window(300, 270, window=Alingmts)

        def show_alineamientos():
            ALI = tk.Label(self, text='C', bg="gray51", fg="red")
            ALI.config(font=('helvetica', 10))
            self.canvas.create_window(400, 270, window=ALI)

            ALI = tk.Label(self, text='A', bg="gray51", fg="blue")
            ALI.config(font=('helvetica', 10))
            self.canvas.create_window(420, 270, window=ALI)

        def get_sequnces():
            seq1 = '-' + entry1.get()
            seq2 = '-' + entry2.get()

            sw = SmithWaterman()
            m, n = sw.run_SW(seq1, seq2)

            Score = tk.Label(self, text=m, font=('helvetica', 10, 'bold'))
            self.canvas.create_window(85, 270, window=Score)

            NumAling = tk.Label(self, text=n[0][0], font=('helvetica', 10, 'bold'))
            self.canvas.create_window(200, 270, window=NumAling)
            show_alineamientos()

        button1 = tk.Button(text='Run', command=get_sequnces,
                                bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        self.canvas.create_window(200, 180, window=button1)

        self.label = tk.Label(self, text="Three page").pack(
                side="top", fill="x", pady=5)
        self.button = tk.Button(
                self, text="Back", command=lambda: master.switch_Canvas(StartUpPage))
        self.button.pack()
        self.canvas.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
