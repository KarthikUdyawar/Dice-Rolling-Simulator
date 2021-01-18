# import
import random
from tkinter import *

class Dice(object):
    def __init__(self,master):
        Frame(master).pack()
        
        self.label = Label(master, font=("times",200))
        Button(master,text="Roll Dice!", command=self.roll,justify=CENTER,font=("times",15)).pack()
        
    def roll(self):
        symbols = ["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]               # Dice in Unicode
        d1,d2 = random.choice(symbols),random.choice(symbols)
        if(d1==d2):
            if(d1=="\u2685"):
                self.label.configure(fg="gold")                                         # if both dice have 6  
            else:
                self.label.configure(fg="medium blue")                                  # if both dice have same number
        else:
            self.label.configure(fg="black")                                            # else black
        self.label.config(text=f"{d1}{d2}")                                             # display dice
        self.label.pack()
        
if __name__ == "__main__":
    root = Tk()
    root.title("Dice Roller")
    root.geometry("500x300")
    Dice(root)
    root.mainloop()