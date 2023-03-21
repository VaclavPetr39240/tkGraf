#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import filedialog
import pylab as pl

# from tkinter import ttk


class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if not "textvariable" in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Hello tkGraf")
        self.lbl.pack()

        self.grafFrame = tk.LabelFrame(self, text='Graf')
        self.grafFrame.pack(padx=5,pady=5,fill='x')


        
        self.fileFrame = tk.LabelFrame(self, text='Soubor')
        self.fileFrame.pack(padx=5, pady=5, fill='x')
        self.fileEntry = MyEntry (self.fileFrame)
        self.fileEntry.pack(fill='x')
        self.fileBtn = tk.Button(self.fileFrame, text='...', command=self.chooseFile)
        self.fileBtn.pack(anchor='e')

        self.dataVar = tk.StringVar(value="ROW")
        self.rowRadio = tk.Radiobutton(self.fileFrame, text='Data jsou v řádcích.', variable=self.dataVar, value="ROW")
        self.rowRadio.pack(anchor='w')
        self.columnRadio = tk.Radiobutton(self.fileFrame, text='Data jsou ve sloupcích.', variable=self.dataVar, value="COLUMN")
        self.columnRadio.pack(anchor='w')


        self.plotBtn = tk.Button(self, text='Graf', command=self.plot)
        self.plotBtn.pack(fill='x')

        self.btn = tk.Button(self, text='Quit', command=self.quit)
        self.btn.pack()


        tk.Label(self.grafFrame, text='Titulek').grid(row=0,column=0)
        self.titleEntry = MyEntry(self.grafFrame)
        self.titleEntry.grid(row=0,column=1)
        tk.Label(self.grafFrame, text='Osa X').grid(row=1,column=0)
        self.xlabelEntry = MyEntry(self.grafFrame)
        self.xlabelEntry.grid(row=1,column=1)
        tk.Label(self.grafFrame, text='Osa Y').grid(row=2,column=0)
        self.ylabelEntry = MyEntry(self.grafFrame)
        self.ylabelEntry.grid(row=2,column=1)


    def chooseFile(self):
       path = filedialog.askopenfilename()
       self.fileEntry.value = path

    def plot(self):
        with open(self.fileEntry.value) as f:
            if self.dataVar.get() == 'ROW':
                line = f.readline()
                x = line.split(';')
                line = f.readline()
                y = line.split(';')
                x = [ float(i.replace(',','.')) for i in x ]
                y = [ float(i.replace(',','.')) for i in y ]
            elif self.dataVar.get() == 'COLUMN':
                x = []
                y = []
                while True:
                    line = f.readline()
                    if line == '':
                        break
                    if ';' not in line:
                        continue
                    x1, y1 = line.split(';')
                    x.append(float(x1.replace(',','.')))
                    y.append(float(y1.replace(',','.')))
        
        pl.plot(x,y)
        pl.title(self.titleEntry.value)
        pl.xlabel(self.xlabelEntry.value)
        pl.ylabel(self.ylabelEntry.value)
        pl.show()
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()