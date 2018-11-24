import tkinter

"""
设置统一的控件风格

"""
# photo = tkinter.PhotoImage(file="d:/untitled/feijitest/res/场景2.png")
# besetyle={
#     "text":checklist,"variable":v,"padx": 1,"pady": 1, "side":left,"fg": "red", "image": photo,
#     "justify": left,"compound": tkinter.CENTER, "font": ("黑体", (20)),"textvariable": v,
#     "variable": v,"value":1,"width": 1,"height": 1,"command": "cammand",activebackground, activeforeground}
# besepack={"padx":1,"pady":1,"ipadx": 1,"ipady": 1,"sticky":tkinter.E}"bitmap":"gray75",
# relief
#
# 指出控件3D效果.可选值为RAISED,SUNKEN,FLAT,RIDGE,SOLID,GROOVE.该值指出控件内部相对于外部的外观样
# 式,比如RAISED意味着控件内部相对于外部突出
#
# 普通风格
COMMONENTRYSTYLE= {"font": ("黑体", (10)),"fg":"black","bg":"white"}
COMMONLABLESTYLE= {"font": ("黑体", (10)),"fg":"black","bg":"#65aefa"}
COMMONTEXTSTYLE={"font": ("黑体", (10)),"fg":"black","bg":"white"}
COMMONFROMESTYLE = {"bg": "#65aefa"}
COMMONBUTTONSTYLE = {"font": ("黑体", (10)),"fg":"black","bg":"#c6d9ed",
"activebackground":"white", "activeforeground":"green"}


style={"font": ("黑体", (10)),"image":None,"fg":"black","bg":"#c6d9ed","text":"1111111",
                        "activebackground":"white", "activeforeground":"green","width":10,"padx":0,"pady":0,
       "height":0,
}


if __name__ == '__main__':
    root=tkinter.Tk(baseName="qqq",className="www",screenName="eee")
    root.resizable(width=False,height=False)
    photo = tkinter.PhotoImage(file="d:/untitled/feijitest/res/场景2.png")
    fromestyle = {"bg": "#65aefa", "width":2, "padx": 20, "pady": 10,
                  "height": 10
                  }
    frome=tkinter.Frame(root,fromestyle)
    frome.pack(padx=0,pady=0)
    b=tkinter.Button(frome,style)
    b1 = tkinter.Button(frome, style)
    b.pack(padx=2,pady=2)
    b1.pack()


    root.mainloop()
    pass
