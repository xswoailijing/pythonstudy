from tkinter import *
sss=True
class tk():
    def __init__(self):
        self.strat=True
    def win(self):
        w=Tk()
        def stop():
            sss=False
        def strat():
            t2.start()
        Button(w,command=strat,text="strat").pack()
        Button(w,command=stop,text="stop").pack()

        t2 = threading.Thread(target=wh().i, args=(1,))
        t2.setDaemon(True)
        t2.start()


        w.mainloop()


class wh():
    def i(self,ii):
        i = 1
        s=tk()
        while i < 100000000000 and sss:
            print(i)
            i +=ii


if __name__ == '__main__':
    # for x in t:
    #     x.setDaemon(True)
    #     x.start()

    tk().win()
    # wh().i()

