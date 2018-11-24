import tkinter
from tkinter import *
import time

tk=tkinter.Tk()
note=Event
note.__init__(note)


def whiletest():

    while True:
        continue
        break

    for a in (1,4):
        continue
        break

class test():
    def __init__(self):
        super().__init__()
        self.a=1
        b=2;c=3

    def u(self,a,b,c,d=0):
        a*=b+c+d
        return a

    def iftest(a):
        a=1
        if a==1:
            pass
        elif a==2:
            pass
        else:
            pass


i=test()
i.mainloop()

print(i.u(1,2,6,9))