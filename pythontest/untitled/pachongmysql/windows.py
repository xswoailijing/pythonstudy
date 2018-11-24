from tkinter import messagebox
from tkinter import *
import os
import sqlconnecttext
from winstyle import *
import mysql
import scan
import project
import proxy
import threading
import time

class tkwindow():

    def __init__(self, winname=None):
        pass

    def rootwindow(self):
        # 主窗口
        rootwindow = self.createwindow()
        rootwindow.resizable(width=False, height=False)
        rootwindow.geometry("1220x650+0+0")
        rootwindow.configure(background="black")
        scan1 = scan.scan()
        proxy1 = proxy.proxy()
        sql = mysql.mysql()
        checkv = IntVar()
        t2=None
        top = Frame(rootwindow, width=1000, height=50, bg="black",)
        top.place(x=0, y=0)
        left = Frame(rootwindow, width=100, height=500, bg="black",)
        left.place(x=0, y=50)
        mid = Frame(rootwindow, width=500, height=500, bg="black",)
        mid.place(x=170, y=50)
        right = Frame(rootwindow, width=300, height=500, bg="black",)
        right.place(x=870, y=50)
        rightlist = Frame(rootwindow, width=300, height=500, bg="black",)
        rightlist.place(x=1050, y=50)
        l = Label(top, font=("楷体", (30)), text="超级图片下载器(Mysql版)", bg="black",fg="white")
        l.place(x=370, y=0)
        roll = Scrollbar(mid)
        midtext = Text(mid, font=("楷体", (10)), height=45, width=96, yscrollcommand=roll.set,bg="black",fg="white")
        roll.config(command=midtext.yview)
        midtext.pack(side=LEFT)
        roll.pack(side=RIGHT, fill=Y)
        def createprojact():
            try:
                sql.linksql()
            except:
                pass
            if sql.sqllink == False:
                tkinter.messagebox.showerror(message="请先连接数据库", title="结果")
                return
            projectname = textproject.get()
            url = texturl.get()
            if url == "" or projectname == "":
                tkinter.messagebox.showerror(message="项目名或网址不能为空", title="结果")
                return
            try:
                p = re.search(r"[a-zA-Z0-9]+", projectname)
                p = p.group()
            except:
                tkinter.messagebox.showerror(message="项目名只能使用大小写字母或数字", title="结果")
                return
            if p != projectname:
                tkinter.messagebox.showerror(message="项目名只能使用大小写字母或数字", title="结果")
                return

            try:
                ret = project.createprojact().createproject(url, projectname)
                if ret == True:
                    tkinter.messagebox.showerror(message="项目已存在", title="结果")
                    return
                pl = open("./projectlist.txt", "r")
                pp = pl.readlines()
                pl.close()
                textlist.delete(0, END)
                for p in pp:
                    textlist.insert(END, p)
                    textmax.delete(0,END)
                    textmax.insert(END, "100")
                    textmax1.delete(0, END)
                    textmax1.insert(END, "100")
                tkinter.messagebox.showinfo(message="%s：\n""项目名%s\n项目地址%s"
                                                    % (ret, projectname, url), title="结果")
            except Exception as error:
                tkinter.messagebox.showerror(message=ret, title="结果")
        def openproject():
            i = textlist.curselection()
            l = textlist.get(i, END)
            textproject.delete(0, END)
            textproject.insert(END, l[0].strip("\n"))
            max = open("./%s/scanset.txt" % textproject.get(), "r")
            ma = max.readlines()
            max.close()
            textmax.delete(0, END)
            textmax.insert(END, ma[1].strip("\n"))
            textmax1.delete(0, END)
            textmax1.insert(END, ma[4].strip("\n"))
            textnow.delete(0, END)
            textnow.insert(END, ma[0].strip("\n"))
            textnow1.delete(0, END)
            textnow1.insert(END, ma[3].strip("\n"))
            textall.delete(0, END)
            textall.insert(END, ma[2].strip("\n"))
        def midtextshow():
            while True:
                while scan1.stop == False or proxy1.strat == True:
                    try:
                        proxy1info = proxy1.info
                        proxy1.info = []
                        for t in proxy1info:
                            midtext.insert(END, t + "\n")
                        proxy1.info = []
                        scan1info = scan1.info
                        scan1.info = []
                        for t in scan1info:
                            midtext.insert(END, t + "\n")
                        projectname = textproject.get()
                        scanset = open("./%s/scanset.txt" % projectname, "r")
                        s = scanset.readlines()
                        scanset.close()
                        textnow.delete(0, END)
                        textnow.insert(END, s[0].strip("\n"))
                        textnow1.delete(0, END)
                        textnow1.insert(END, s[3].strip("\n"))
                        textall.delete(0, END)
                        textall.insert(END, s[2].strip("\n"))
                        midtext.yview_moveto(1)
                        time.sleep(1)
                    except:
                        pass
                time.sleep(1)
        t1 = threading.Thread(target=midtextshow)
        t1.setDaemon(True)
        t1.start()
        def startscan():
            projectname = textproject.get()
            reurl = r"http[A-Za-z0-9._+/:\-]+"
            try:
                sql.linksql()
            except:
                pass
            if sql.sqllink == False:
                tkinter.messagebox.showerror(message="请先连接数据库", title="结果")
                return
            if scan1.stop == False:
                tkinter.messagebox.showerror(message="请先停止当前进程", title="结果")
                return
            projectlist = open("./projectlist.txt", "r")
            pl = projectlist.readlines()
            projectlist.close()
            if len(pl) == 0:
                tkinter.messagebox.showerror(message="请先创建项目", title="结果")
                return
            for l in pl:
                if l.strip("\n") == projectname:
                    max = open("./%s/scanset.txt" % projectname, "r")
                    ma = max.readlines()
                    max.close()
                    max = open("./%s/scanset.txt" % projectname, "w+")
                    ma[1] = "%s\n" % textmax.get()
                    ma[4] = "%s\n" % textmax1.get()
                    ma[0] = "%s\n" % textnow.get()
                    ma[3] = "%s\n" % textnow1.get()
                    for m in ma:
                        max.write(m)
                    max.close()
                    thread = int(textthread.get())
                    scan1.stop = False
                    t2 = threading.Thread(target=scan1.allrun, args=(projectname, reurl, bool(checkv.get()), thread,))
                    t2.setDaemon(True)
                    t2.start()



                    return
            tkinter.messagebox.showerror(message="项目不存在", title="结果")
        def stopscan():
            scan1.stop = True
            midtext.insert(END,"正在停止进程.......请稍等.\n")
            t2.join()
            midtext.yview_moveto(1)
        def delproject():
            projectname = textproject.get()
            if projectname == "":
                tkinter.messagebox.showerror(message="请选择要删除的项目", title="结果")
                return
            try:
                ret = project.createprojact().delproject(projectname)
                pl = open("./projectlist.txt", "r")
                pp = pl.readlines()
                pl.close()
                textlist.delete(0, END)
                for p in pp:
                    textlist.insert(0, p)
                tkinter.messagebox.showinfo(message=ret, title="结果")
            except Exception as error:
                tkinter.messagebox.showerror(message="删除失败%s" % error, title="结果")
        def openpath():
            os.system(r"explorer.exe %s\%s" % (os.sys.path[0], textproject.get()))
        b0 = Button(right, font=("楷体", (15)),bg="black",fg="white", height=1, text="开始扫描", command=startscan)
        b0.pack(pady=2)
        b0 = Button(right, font=("楷体", (15)),bg="black",fg="white", height=1, text="停止扫描", command=stopscan)
        b0.pack(pady=2)
        b0 = Button(right, font=("楷体", (15)),bg="black",fg="white", height=1, text="打开项目文件夹", command=openpath)
        b0.pack(pady=2)
        Label(right, font=("楷体", (15)), text="项目名称", bg="black",fg="white").pack(pady=2)
        textproject = Entry(right, width=20)
        textproject.pack(pady=2, padx=10)
        Label(right, font=("楷体", (15)), text="项目根网址", bg="black",fg="white").pack(pady=2)
        texturl = Entry(right)
        texturl.pack(pady=2, padx=10)
        texturl.insert(END, "https://")
        b0 = Button(right, font=("楷体", (15)),bg="black",fg="white", height=1, text="创建项目", command=createprojact)
        b0.pack(pady=2)
        b0 = Button(right, font=("楷体", (15)),bg="black",fg="white", height=1, text="删除项目", command=delproject)
        b0.pack(pady=2)
        Label(right, font=("楷体", (10)), text="设置扫描网址数上限\n(扫描到后停止)", bg="black",fg="white").pack(pady=2)
        textmax = Entry(right)
        textmax.pack(pady=2, padx=10)
        textmax.insert(END, "100")
        Label(right, font=("楷体", (10)), text="设置开始扫描网址编号\n(不能大于总获得网址数)", bg="black",fg="white").pack(pady=2)
        textnow = Entry(right)
        textnow.pack(pady=2, padx=10)
        textnow.insert(END, "0")
        Label(right, font=("楷体", (10)), text="设置下载图片数上限", bg="black",fg="white").pack(pady=2)
        textmax1 = Entry(right)
        textmax1.pack(pady=2, padx=10)
        textmax1.insert(END, "100")
        Label(right, font=("楷体", (10)), text="当前已下载图片数", bg="black",fg="white").pack(pady=2)
        textnow1 = Entry(right)
        textnow1.pack(pady=2, padx=10)
        textnow1.insert(END, "0")
        Label(right, font=("楷体", (15)), text="总获得网址数", bg="black",fg="white").pack(pady=2)
        textall = Entry(right)
        textall.pack(pady=2, padx=10)
        textall.insert(END, "0")



        def setmysql():
            self.mysqlconnectwindow()

        def upproxy():

            url = textproxy.get()
            t3 = threading.Thread(target=proxy1.upproxylistfile, args=(url, 3,))
            t3.setDaemon(True)
            t3.start()

        def addproxy():
            pass

        def optimizeproxy():
            url = texttestproxy.get()
            proxy1.strat = True
            t4 = threading.Thread(target=proxy1.testproxylistfile, args=(url, 150,))
            t4.setDaemon(True)
            t4.start()
            t1 = threading.Thread(target=midtextshow)
            t1.setDaemon(True)
            t1.start()

        def stopoptimizeproxy():
            proxy1.strat = False

        def clearproxy():
            file = open("%s/" % os.sys.path[0] + "proxyiplist/proxyip.txt", "w")
            file.writelines("")
            file.close()
            messagebox.showinfo(message="已清空!", title="清除代理")

        Button(left, font=("楷体", (15)),bg="black",fg="white", height=1, text="从网站更新代理", command=upproxy).pack(pady=2, padx=10)
        Label(left, font=("楷体", (10)), text="代理更新网站设置", bg="black",fg="white").pack(pady=2)
        textproxy = Entry(left)
        textproxy.pack(pady=2, padx=10)
        textproxy.insert(END, "http://demo.docmobile.cn/http")
        Button(left, font=("楷体", (15)),bg="black",fg="white", height=1, text="手动添加代理", ).pack(pady=2)
        Button(left, font=("楷体", (15)),bg="black",fg="white", height=1, text="清空所有代理地址", command=clearproxy).pack(pady=2)
        Button(left, font=("楷体", (15)),bg="black",fg="white", height=1, text="筛选优化代理", command=optimizeproxy).pack(pady=2)
        Button(left, font=("楷体", (15)),bg="black",fg="white", height=1, text="停止筛选优化代理", command=stopoptimizeproxy).pack(pady=2)
        Label(left, font=("楷体", (10)), text="筛选测试网站", bg="black",fg="white").pack(pady=2)
        texttestproxy = Entry(left)
        texttestproxy.pack(pady=2, padx=10)
        texttestproxy.insert(END, "http://www.baidu.com")
        Label(rightlist, font=("楷体", (12)), text="设置线程数.\n(线程越大下载\n图片速度越快，\n根据机器配置与\n网络情况设置，\n建议在100-1000之间)",
              bg="black",fg="white").pack(pady=2)
        textthread = Entry(rightlist, width=20)
        textthread.pack(pady=2, padx=10)
        textthread.insert(END, 10)
        Label(rightlist, font=("楷体", (15)),bg="black",fg="white", height=1, text="已有项目列表").pack(pady=2)
        textlist = tkinter.Listbox(rightlist, height=10)
        textlist.pack(pady=2, padx=10)
        try:
            pl = open("./projectlist.txt", "r")
            pp = pl.readlines()
            pl.close()
            for p in pp:
                textlist.insert(END, p)
        except:
            pass
        b0 = Button(rightlist, font=("楷体", (15)),bg="black",fg="white", height=1, text="使用项目", command=openproject)
        b0.pack(pady=2)
        Checkbutton(rightlist, font=("楷体", (10)),
                    text="使用代理\n(部分网站有反爬功能\n设置代理可防止被封IP)", bg="black",fg="red",
                    variable=checkv).pack(pady=2)
        Label(rightlist, font=("楷体", (15)),bg="black",fg="white", height=1, text="扫描模式", ).pack(pady=2)
        radiov = IntVar()
        Radiobutton(rightlist, font=("楷体", (10)), text="只扫描此地址", bg="black",fg="yellow"
                    , variable=radiov, value=0).pack(pady=2, anchor=W)
        Radiobutton(rightlist, font=("楷体", (10)), text="只扫描此网站内", bg="black",fg="yellow"
                    , variable=radiov, value=1).pack(pady=2, anchor=W)
        Radiobutton(rightlist, font=("楷体", (10)), text="全网扫描\n(百度模式扫描，\n以设置的网址为根地址)"
                    , variable=radiov, value=2, bg="black",fg="yellow").pack(pady=2, anchor=W)
        Label(left, font=("楷体", (10)), text="版本信息:\n"
                                            "版本.0.1test\n"
                                            "用于学习Pthon编码\n"
                                            "特性的手工无框架版\n"
                                            "网站图片爬虫。\n"
                                            "出品人:MR.ZHOU.\n"
                                            "邮箱:542945190@qq.com", bg="black", fg="white").pack(pady=2)
        Button(left, font=("楷体", (15)),bg="black",fg="red", height=1, text="配置数据库", command=setmysql).pack(pady=2, anchor=S)

        return rootwindow

    def mysqlconnectwindow(self):
        """
        创建数据库窗口
        :return:
        """
        labletext = sqlconnecttext.SQLCONNECTTEXT_CN
        sqlwin = Tk()
        # sqlwin.resizable(width=False, height=False)
        sqlwin.configure(background="black")
        sqlwin.geometry("460x500+100+100")
        ##################################################################################################
        top = Frame(sqlwin, width=300, height=50, bg="black")
        top.place(x=20, y=0)
        left = Frame(sqlwin, width=100, height=500, bg="black",)
        left.place(x=0, y=50)
        rigth = Frame(sqlwin, width=300, height=500, bg="black",)
        rigth.place(x=250, y=55)
        bottom = Frame(sqlwin, width=300, height=50, bg="black",)
        bottom.place(x=200, y=450)
        ##################################################################################################
        Label(top, font=("楷体", (15)), bg="black",fg="white", text="创建数据库，请确认已经正确安装mysql数据库！").pack(side=TOP)
        for lable in labletext:
            Label(left, font=("楷体", (15)), bg="black",fg="white", text=lable).pack(pady=19, anchor=E)
        host = Entry(rigth, font=("楷体", (15)))
        host.pack(pady=20)
        user = Entry(rigth, font=("楷体", (15)))
        user.pack(pady=20)
        passwd = Entry(rigth, font=("楷体", (15)))
        passwd.pack(pady=20)
        db = Entry(rigth, font=("楷体", (15)))
        db.pack(pady=20)
        prot = Entry(rigth, font=("楷体", (15)))
        prot.pack(pady=20)
        charset = Entry(rigth, font=("楷体", (15)))
        charset.pack(pady=20)
        host.insert(END, "127.0.0.1")
        user.insert(END,"root")
        db.insert(tkinter.END, "superimage")
        prot.insert(tkinter.END, "3306")
        charset.insert(tkinter.END, "utf8")

        def cmd():
            result = mysql.mysql().createsql(dbhost=host.get(), dbname=db.get(), dbuser=user.get(),
                                             dbpassword=passwd.get(), dbport=int(prot.get()), charset=charset.get())
            if result == True:
                tkinter.messagebox.showinfo(message="数据库创建成功", title="结果")
                dbinfo = [host.get(), db.get(), user.get(),
                          passwd.get(), prot.get(), charset.get()]
                d = open("./dbinfo.txt", "w+")
                for di in dbinfo:
                    d.write("%s\n" % di)
                d.close()
            else:
                tkinter.messagebox.showinfo(message=result, title="结果")

        Button(bottom, text="创建数据库", command=cmd).pack(anchor=CENTER)
        return sqlwin

    def listbox(self):
        # 列表框
        pass

    def createScrollbar(self, frame, style=None):

        roll = tkinter.Scrollbar(frame, style)
        return roll

    def createwindow(self, winname=None):
        # 创建窗口
        window = tkinter.Tk()
        window.title = winname
        return window

    def createframe(self, windowhandle, style=None):
        # 窗口容器
        frome = tkinter.Frame(windowhandle, style)
        return frome

    def createtext(self, frame, style=None):
        # 文本框
        textinput = tkinter.Text(frame, style)
        return textinput

    def creatrentry(self, frame, style=None):
        # 输入框
        entey = tkinter.Entry(frame, style)
        return entey

    def createcheckbutton(self, frame, style=None):
        check = tkinter.Checkbutton(frame, style)
        return check
        # 复选框

    def createLabel(self, frame, style=None):
        lable = tkinter.Label(frame, style)
        return lable
        # 标签

    def createradiobutton(self, frame, style=None):
        radio = tkinter.Radiobutton(frame, style)
        return radio
        # 单选框

    def lableframe(self, frame, style=None):
        group = tkinter.LabelFrame(frame, style)
        return group
        # 标签容器

    def createButton(self, frame, style=None):
        button = tkinter.Button(frame, style)
        return button
        # 按钮

    def testbutton(self):
        print("按钮测试")


if __name__ == '__main__':
    t=tkwindow()
    pass



