import tkinter as tk
from tkinter import filedialog
import pylab as pl

load = {}
osax=[]
osay=[]
pocet = 0

"""
soubor = filedialog.askopenfilename(title="Vyber soubor", initialdir=".")
with open(soubor, "r") as t:
    for line in t.readlines():
        line = line.strip()
        line = line.split()
        pocet = pocet + 1
        load.update({line[0] : line[1]})


for key in load.keys():
    x = key
    y = load[key]
    print(x)
    print(y)
    print("bod")
    osax.append(float(x))
    osay.append(float(y))
    
pl.plot(osax,osay)
pl.title("Graf ze souboru")
pl.show()
"""
class Application(tk.Tk):
    name = "Graf ze souboru - nástroj"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        
        self.load_button = tk.Button(self, text="Zdroj", command=self.zdroj)
        self.load_button.pack()
        self.generate_button = tk.Button(self, text="Generace", command=self.gener)
        self.generate_button.pack()
        self.end_button = tk.Button(self, text="Zavřít", command=self.quit)
        self.end_button.pack()
        
    def zdroj(self):
        global load
        global osax
        global osay
        global pocet
                
        soubor = filedialog.askopenfilename(title="Vyber soubor", initialdir=".")
        with open(soubor, "r") as t:
            for line in t.readlines():
                line = line.strip()
                line = line.split()
                pocet = pocet + 1
                load.update({line[0] : line[1]})


        for key in load.keys():
            x = key
            y = load[key]
            #print(x)
            #print(y)
            #print("bod")
            osax.append(float(x))
            osay.append(float(y))

    def gener(self):
        global osax
        global osay
        pl.plot(osax,osay)
        pl.title("Graf ze souboru")
        pl.show()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()