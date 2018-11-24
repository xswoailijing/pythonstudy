import pymysql
import tkinter
from tkinter import messagebox
from tkinter import *
import urllib.request
import threading
import random
import time
import re
import hashlib
import os

SQLCONNECTTEXT_CN = [
    "HOST(SQL地址):",
    "USER(用户名):",
    "PASSWD(密码):",
    "DB(数据库名):",
    "PORT(端口):",
    "CHARSET(数据库默认编码):"
]


class Openurltofile():
    def __init__(self):
        self.info = []

    def imagedownload(self, projectname, type, url, timeout):
        try:
            image = urllib.request.urlopen(url, timeout=timeout)
            image1 = image.read()
            md5 = hashlib.md5(image1)
            md5 = md5.hexdigest()
            with open("./%s/%s%s" % ( projectname, md5, type), "wb") as f:
                f.write(image1)
                f.close()
                print("图片%s已下载且重命名为%s" % (url, "./%s/%s%s" % ( projectname, md5, type)))
                self.info = ("图片%s已下载且重命名为%s" % (url, "./%s/%s%s" % ( projectname, md5, type)))
                return "./%s/%s%s" % ( projectname, md5, type)
        except Exception as error:
            print("图片%s未能下载%s" % (url, error))
            self.info = ("图片%s未能下载%s" % (url, error))
            return False


class Projact():
    def __init__(self):
        self.mysql = Mysql()
    def createproject(self, url, projectname):
        # 创建项目
        if os.path.exists("./" + "/" + projectname):
            print("项目已经存在。")
            return True
        else:
            try:
                self.mysql.createproject(projectname)
                os.mkdir("./" + "/" + projectname)
                projectlist = open("./" + "/projectlist.txt", "a")
                projectlist.write(projectname + "\n")
                projectlist.close()
                config = open("./" + "/" + projectname + "/scanset.txt", "w")
                config.write("0\n"  # urlstart:
                             "100\n"  # urlend:
                             "0\n"  # urlline:
                             "0\n"  # imagestart: 
                             "100\n"  # imageend:
                             "5\n"  # opentimeout
                             "5\n"  # retry
                             "gbk\n"  # opencoding
                             "utf8\n"  # inputcoding
                             + url + "\n"
                             )
                config.close()
                print("创建项目成功")
                return "创建项目成功"
            except Exception as error:
                print("创建项目失败%s" % error)
                return "创建项目失败%s" % error

    def delproject(self, projectname):
        if os.path.exists("./" + "/" + projectname):
            try:
                listdir = os.listdir("./" + "/" + projectname)
                for l in listdir:
                    os.remove("./" + "/" + projectname + "/" + l)
                os.rmdir("./" + "/" + projectname)
                self.mysql.delproject(projectname)
                projectlist0 = open("./" + "/projectlist.txt", "r")
                projectlist0.readlines()
                projectlist1 = open("./" + "/projectlist.txt", "w+")
                for l in projectlist0:
                    if l.strip("\n") != projectname:
                        projectlist1.write(l + "\n")
                projectlist1.close()
                print("项目%s删除成功" % projectname)
                return "项目%s删除成功" % projectname
            except Exception as error:
                print("项目%s删除失败%s" % (projectname, error))
                return "项目%s删除失败错误%s" % (projectname, error)
        else:
            return "项目不存在"

    def projectset(self, hards):
        # 反爬设置
        self.hards = {
            "User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"

        }


class Proxy():
    def __init__(self):
        self.proxyiplist = []
        self.info = []
        self.strat = False

    def testproxylistfile(self, testurl, timeout):
        """
        读取一个文本文件内的ip列表,测试其每一个的连接状态
        文件中不能有空白行
        :param proxyiplistlfile: 文件名
        :param timeout: 设置最大延迟时间，大于此延迟的被抛弃
        """
        # 清空以前使用的代理服务列表
        file = open("./proxyiplist/runproxyurl.txt", "w")
        file.writelines("")
        file.close()
        i = 0
        with open("./proxyiplist/proxyip.txt", "r") as file:
            while self.strat:
                testproxyip = file.readline().strip("\n")
                if len(testproxyip) == 0:
                    file.close()
                    break
                else:
                    # # 尝试用http连接
                    # testproxyurlhttp = {"http:": testproxyip}
                    # try:
                    #     proxyreosd = urllib.request.ProxyHandler(testproxyurlhttp)
                    #     opener = urllib.request.build_opener(proxyreosd)
                    #     urllib.request.install_opener(opener)
                    #     print("待测试%s代理设置成功" % testproxyurlhttp)
                    #     try:
                    #         t1=time.time()
                    #         r =urllib.request.urlopen(testurl,timeout=timeout)
                    #         t2=time.time()
                    #         t=(t2-t1)*1000
                    #         if t< timeout:
                    #             with open("%s/"%os.sys.path[0]+"proxyiplist/runproxyurl.txt", "a") as filehttpw:
                    #                 filehttpw.writelines("http:" + testproxyip + "\n")
                    #                 filehttpw.close()
                    #                 i += 1
                    #                 print("连接到%s时延迟%sms，已加入代理队列" % (testproxyurlhttp, t))
                    #         else:
                    #             print("连接%s时延迟%sms过高.. 抛弃使用" % (testproxyurlhttp, t))
                    #     except:
                    #         print("此代理服务器地址不能连接到网络%s已抛弃" % testproxyurlhttp)
                    # except:
                    #     print("尝试设置测试IP%s失败")

                    # 尝试用https连接
                    testproxyurlhttp = {"https:": testproxyip}
                    try:
                        proxyreosd = urllib.request.ProxyHandler(testproxyurlhttp)
                        opener = urllib.request.build_opener(proxyreosd)
                        urllib.request.install_opener(opener)
                        print("待测试%s代理设置成功" % testproxyurlhttp)
                        self.info.append("待测试%s代理设置成功" % testproxyurlhttp)
                        try:
                            t1 = time()
                            r = urllib.request.urlopen(testurl, timeout=timeout)
                            t2 = time()
                            t = (t2 - t1) * 1000
                            if t < timeout:
                                with open("./proxyiplist/runproxyurl.txt", "a") as filehttpw:
                                    filehttpw.writelines("https:" + testproxyip + "\n")
                                    filehttpw.close()
                                    i += 1
                                    print("连接到%s时延迟%sms，已加入代理队列" % (testproxyurlhttp, t))
                                    self.info.append("连接到%s时延迟%sms，已加入代理队列" % (testproxyurlhttp, t))
                            else:
                                print("连接%s时延迟%sms过高.. 抛弃使用" % (testproxyurlhttp, t))
                                self.info.append("连接%s时延迟%sms过高.. 抛弃使用" % (testproxyurlhttp, t))
                        except:
                            print("此代理服务器地址不能连接到网络%s已抛弃" % testproxyurlhttp)
                            self.info.append("此代理服务器地址不能连接到网络%s已抛弃" % testproxyurlhttp)
                    except:
                        print("尝试设置测试IP%s失败")
                        self.info.append("尝试设置测试IP%s失败")
        print("代理服务器筛选完成。。共添加%s个可用代理服务器地址" % i)
        self.info.append("代理服务器筛选完成。。共添加%s个可用代理服务器地址" % i)
        file.close()

    def setproxylistfile(self):
        """
            从文本文件中随机抽取一行IP地址作为代理地址，
            文本格式为每行127.0.0.1:80或192.0.0.1均可
        :param proxyiplistlfile: 保存ip地址列表的文件名
        """

        proxyiplist = []
        with open("./proxyiplist/runproxyurl.txt", "r") as file:
            while True:
                proxyip = file.readline().strip("\n")
                if len(proxyip) == 0:
                    file.close()
                    break
                else:
                    http = re.search(r"http[s]{0,1}", proxyip)
                    ip = re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]{0,5}", proxyip)
                    dict = {http.group(): ip.group()}
                    proxyiplist.append(dict)
                    print(proxyiplist)
        print("代理列表已设置")
        self.info.append("代理列表已设置")
        file.close()
        return proxyiplist

    def proxystrat(self, proxylist):
        """
        接收一个url字典列表，尝试使用此列表内的ip地址字典进行代理设置
        :param proxylist: ip列表
        :return: 返回0成功，返回1失败
        """
        if len(proxylist) > 0:
            proxyip = random.choice(proxylist)
            try:
                proxyreosd = urllib.request.ProxyHandler(proxyip)
                opener = urllib.request.build_opener(proxyreosd)
                urllib.request.install_opener(opener)
                print("%s代理设置成功" % proxyip)
                return "%s代理设置成功" % proxyip
            except Exception as error:
                print("尝试设置IP%s失败%", error)
                return "尝试设置IP%s失败%", error
        else:
            print("代理列表为空，代理失败，使用本机ip访问")
            return "代理列表为空，代理失败，使用本机ip访问"

    def upproxylistfile(self, url, timaout=3):
        """
            从设置的网址读取代理列表
        :param url:
        :param timaout:
        :return:
        """
        file = "%s/proxyiplist/updataproxyip.txt" % os.sys.path[0]
        with open(file, "w", encoding="utf8") as file:
            try:
                txtfile = urllib.request.urlopen(url, timeout=timaout)
                print("读取网站成功")
                self.info.append("读取网站成功")
                txtfile = txtfile.read()
                txtfile = txtfile.decode("utf8")
                file.write(txtfile)
                file.close()
                print("已获得%s代理资料。。等待添加" % url)
                self.info.append("已获得%s代理资料。。等待添加" % url)
            except Exception as eroor:
                file.close()
                print("代理ip更新服务器%s无法连接。。。%s" % (url, eroor))
                self.info.append("代理ip更新服务器%s无法连接。。。%s" % (url, eroor))
                return
        with open("./proxyiplist/updataproxyip.txt"  "r", encoding="utf8") as file:
            i = 1
            while True:
                proxylist = file.readline()
                if len(proxylist) == 0:
                    file.close()
                    break
                else:
                    r1 = re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", proxylist)
                    r2 = re.search(r":[0-9]{0,5}", proxylist)
                    if r1 != None and r2 != None:
                        r = r1.group() + r2.group() + "\n"
                        addfile = open("./proxyiplist/proxyip.txt" "a")
                        addfile.writelines(r)
                        addfile.close()
                        i += 1
            file.close()
            print("添加%s个代理服务器地址成功" % (i - 1))
            self.info.append("添加%s个代理服务器地址成功" % (i - 1))

    def addproxylist(self, proxyfile):
        """
        每行文件中包含ip地址和端口号的自动添加到代理地址库端口号前要加：
        无端口号则默认80或8080

        :param proxyfile: 要添加的文件名
        """
        # 手动添加代理列表
        with open(proxyfile, "r", encoding="utf8") as file:
            i = 0
            while True:
                proxylist = file.readline()
                if len(proxylist) == 0:
                    file.close()
                    break
                else:
                    r1 = re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", proxylist).group()
                    r2 = re.search(r":[0-9]{0,5}", proxylist).group()
                    r = r1 + r2 + "\n"
                    addfile = open("%s/proxyiplist/proxyip.txt" % os.sys.path[0], "a")
                    addfile.writelines(r)
                    addfile.close()
                    i += 1
        file.close()
        print("添加%s个代理服务器地址成功" % i)
        self.info.append("添加%s个代理服务器地址成功" % i)


class Scan(object):
    def __init__(self):
        self.info = []
        self.stop = True

    def allrun(self, projectname, reurl, proxy_set=False, thread=1, out=False):
        """
         用于顺序扫描根网页下所有链接的方法
        :param projectname: 扫描对象的名称
        :param reurl: 正则过滤
        :param proxy_set: 判断是否使用代理
        :param thread: 线程数
        :param out: 判断是否允许爬出根网址
        :return:
        """
        proxyiplist = []
        imagedownload1 = Openurltofile()
        sql=Mysql()
        # 读取配置文件
        f = open("./%s/scanset.txt" %  projectname, "r")
        configlist = f.readlines()
        f.close()
        timeout = int(configlist[6].strip("\n"))
        # 判断是否使用代理
        if proxy_set == True:
            proxyiplist = Proxy().setproxylistfile()
        # 初始化多线程参数
        sc = []
        textdatautf8 = []
        textdatagbk = []
        th = []
        imaged = []
        path = []
        urldata = []
        u = []
        for i in range(0, thread):
            u.append(None)
            path.append(False)
            sc.append(True)
            textdatautf8.append(None)
            textdatagbk.append(None)
            th.append(True)
            imaged.append(False)
        # 测试根网址
        u[0] = configlist[9].strip("\n")
        try:
            urltext = urllib.request.urlopen(u[0], timeout=3)
            text = urltext.read()
            try:
                textdatautf8[0] = text.decode(configlist[8].strip("\n"))
            except:
                pass
            try:
                textdatagbk[0] = text.decode(configlist[7].strip("\n"))
            except:
                pass
        except Exception as error:
            print("根网页%s无法打开%s" % (configlist[9].strip("\n"), error))
            self.info.append("根网页%s无法打开%s" % (configlist[9].strip("\n"), error))
            return
        # 开始循环扫描
        while (int(configlist[0]) < int(configlist[1])) and \
                (int(configlist[3]) < int(configlist[4])) and \
                self.stop == False:
            # 多线程回调函数
            def scan(url, t):
                sc[t] = False
                self.info.append(Proxy().proxystrat(proxyiplist))
                ########################################################################################################################
                try:
                    url.index(".jpg")
                    path[t] = imagedownload1.imagedownload(projectname, ".jpg", url, timeout)
                    imaged[t] = True
                    sc[t] = True
                    self.info.append(imagedownload1.info)
                    return
                except:
                    pass
                #########################################################################################################################
                try:
                    url.index(".gif")
                    path[t] = imagedownload1.imagedownload(projectname, ".gif", url, timeout)
                    imaged[t] = True
                    sc[t] = True
                    self.info.append(imagedownload1.info)
                    return
                except:
                    pass
                ##########################################################################################################################
                try:
                    url.index(".png")
                    path[t] = imagedownload1.imagedownload(projectname, ".png", url, timeout)
                    imaged[t] = True
                    sc[t] = True
                    self.info.append(imagedownload1.info)
                    return
                except:
                    pass
                #########################################################################################################################
                # 读取url数据
                try:
                    urltext = urllib.request.urlopen(u[i], timeout=3)
                    text = urltext.read()
                    try:
                        textdatautf8[t] = text.decode(configlist[8].strip("\n"))
                    except:
                        pass
                    try:
                        textdatagbk[t] = text.decode(configlist[7].strip("\n"))
                    except:
                        pass
                    sc[t] = True
                    self.info.append(imagedownload1.info)
                except Exception as  error:
                    print("网页%s无法打开...%s" % (url, error))
                    self.info.append("网页%s无法打开...%s" % (url, error))
                    self.info.append(imagedownload1.info)
                sc[t] = True
                #########################################################################################################################
                # 读取缓存中的url保存到数据表

            i = 0
            while i < thread:
                if sc[i] == True:
                    if imaged[i]:
                        sql.inputimagepath(u[i], path[i], projectname)
                        self.info.append(sql.info)
                        configlist[3] = "%s\n" % (int(configlist[3].strip("\n")) + 1)
                        print("抽取到%s张图片%s" % (configlist[3], u[i]))
                    if path[i] is False and textdatautf8[i] is not None and textdatautf8[i] is not bytes:
                        try:
                            sql.inputtextdata(u[i], projectname, textdatautf8[i])
                        except Exception as error:
                            print("网页%sutf8编码写入错误%s" % (u[i]), error)
                            self.info.append("网页%sutf8编码写入错误%s" % (u[i]), error)
                            try:
                                sql.inputtextdata(u[i], projectname, textdatagbk[i])
                            except Exception as error:
                                print("网页%sgbk编码写入错误%s" % (u[i]), error)
                                self.info.append("网页%sgbk编码写入错误%s" % (u[i]), error)
                        try:
                            urldata = re.findall(reurl, textdatautf8[i])
                            for urlline in urldata:
                                urlinput = sql.inputurl(projectname, int(configlist[2].strip("\n")), urlline)
                                if urlinput == True:
                                    configlist[2] = "%s\n" % str(int(configlist[2].strip("\n")) + 1)
                                    print("共储存%s个地址" % configlist[2].strip("\n"))
                        except:
                            try:
                                if textdatagbk[i] is not None and textdatagbk[i] is not bytes:
                                    urldata = re.findall(reurl, textdatagbk[i])
                                    for urlline in urldata:
                                        urlinput = sql.inputurl(projectname, int(configlist[2].strip("\n")), urlline)
                                        if urlinput == True:
                                            configlist[2] = "%s\n" % str(int(configlist[2].strip("\n")) + 1)
                                            print("共储存%s个地址" % configlist[2].strip("\n"))
                            except:
                                pass
                    if int(configlist[0]) < int(configlist[2]):
                        u[i]=sql.readurl(projectname,int(configlist[0].strip("\n")))[1]
                        configlist[0] = "%s\n" % (int(configlist[0].strip("\n")) + 1)
                        print("已爬行%s个页面" % configlist[0].strip("\n"))
                        self.info.append("已爬行%s个页面" % configlist[0].strip("\n"))
                    th[i] = threading.Thread(target=scan, args=(u[i], i,))
                    th[i].setDaemon(True)
                    th[i].start()
                    i += 1
                    with open("./%s/scanset.txt" % projectname, "w+") as f:
                        for li in configlist:
                            f.write("%s" % li)
                        f.close()

            self.info = ["0"]
class TKwindow():

    def __init__(self, winname=None):
        pass

    def rootwindow(self):
        # 主窗口
        rootwindow = Tk()
        rootwindow.resizable(width=False, height=False)
        rootwindow.geometry("1220x650+0+0")
        rootwindow.configure(background="black")
        scan1 = Scan()
        proxy1 = Proxy()
        sql = Mysql()
        project_0=Projact()
        sql.linksql()
        checkv = IntVar()
        t2 = None
        top = Frame(rootwindow, width=1000, height=50, bg="black", )
        top.place(x=0, y=0)
        left = Frame(rootwindow, width=100, height=500, bg="black", )
        left.place(x=0, y=50)
        mid = Frame(rootwindow, width=500, height=500, bg="black", )
        mid.place(x=170, y=50)
        right = Frame(rootwindow, width=300, height=500, bg="black", )
        right.place(x=870, y=50)
        rightlist = Frame(rootwindow, width=300, height=500, bg="black", )
        rightlist.place(x=1050, y=50)
        l = Label(top, font=("楷体", (30)), text="超级图片下载器(Mysql版)", bg="black", fg="white")
        l.place(x=370, y=0)
        roll = Scrollbar(mid)
        midtext = Text(mid, font=("楷体", (10)), height=45, width=96, yscrollcommand=roll.set, bg="black", fg="white")
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
                ret = project_0.createproject(url, projectname)
                if ret == True:
                    tkinter.messagebox.showerror(message="项目已存在", title="结果")
                    return
                pl = open("./projectlist.txt", "r")
                pp = pl.readlines()
                pl.close()
                textlist.delete(0, END)
                for p in pp:
                    textlist.insert(END, p)
                    textmax.delete(0, END)
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
            midtext.insert(END, "正在停止进程.......请稍等.\n")
            t2.join()
            midtext.yview_moveto(1)

        def delproject():
            projectname = textproject.get()
            if projectname == "":
                tkinter.messagebox.showerror(message="请选择要删除的项目", title="结果")
                return
            try:
                ret = project_0.delproject(projectname)
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
            os.system(r"explorer.exe ./%s" %textproject.get())

        b0 = Button(right, font=("楷体", (15)), bg="black", fg="white", height=1, text="开始扫描", command=startscan)
        b0.pack(pady=2)
        b0 = Button(right, font=("楷体", (15)), bg="black", fg="white", height=1, text="停止扫描", command=stopscan)
        b0.pack(pady=2)
        b0 = Button(right, font=("楷体", (15)), bg="black", fg="white", height=1, text="打开项目文件夹", command=openpath)
        b0.pack(pady=2)
        Label(right, font=("楷体", (15)), text="项目名称", bg="black", fg="white").pack(pady=2)
        textproject = Entry(right, width=20)
        textproject.pack(pady=2, padx=10)
        Label(right, font=("楷体", (15)), text="项目根网址", bg="black", fg="white").pack(pady=2)
        texturl = Entry(right)
        texturl.pack(pady=2, padx=10)
        texturl.insert(END, "https://")
        b0 = Button(right, font=("楷体", (15)), bg="black", fg="white", height=1, text="创建项目", command=createprojact)
        b0.pack(pady=2)
        b0 = Button(right, font=("楷体", (15)), bg="black", fg="white", height=1, text="删除项目", command=delproject)
        b0.pack(pady=2)
        Label(right, font=("楷体", (10)), text="设置扫描网址数上限\n(扫描到后停止)", bg="black", fg="white").pack(pady=2)
        textmax = Entry(right)
        textmax.pack(pady=2, padx=10)
        textmax.insert(END, "100")
        Label(right, font=("楷体", (10)), text="设置开始扫描网址编号\n(不能大于总获得网址数)", bg="black", fg="white").pack(pady=2)
        textnow = Entry(right)
        textnow.pack(pady=2, padx=10)
        textnow.insert(END, "0")
        Label(right, font=("楷体", (10)), text="设置下载图片数上限", bg="black", fg="white").pack(pady=2)
        textmax1 = Entry(right)
        textmax1.pack(pady=2, padx=10)
        textmax1.insert(END, "100")
        Label(right, font=("楷体", (10)), text="当前已下载图片数", bg="black", fg="white").pack(pady=2)
        textnow1 = Entry(right)
        textnow1.pack(pady=2, padx=10)
        textnow1.insert(END, "0")
        Label(right, font=("楷体", (15)), text="总获得网址数", bg="black", fg="white").pack(pady=2)
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
            file = open("./proxyiplist/proxyip.txt", "w")
            file.writelines("")
            file.close()
            messagebox.showinfo(message="已清空!", title="清除代理")

        Button(left, font=("楷体", (15)), bg="black", fg="white", height=1, text="从网站更新代理", command=upproxy).pack(pady=2,
                                                                                                                padx=10)
        Label(left, font=("楷体", (10)), text="代理更新网站设置", bg="black", fg="white").pack(pady=2)
        textproxy = Entry(left)
        textproxy.pack(pady=2, padx=10)
        textproxy.insert(END, "http://demo.docmobile.cn/http")
        Button(left, font=("楷体", (15)), bg="black", fg="white", height=1, text="手动添加代理", ).pack(pady=2)
        Button(left, font=("楷体", (15)), bg="black", fg="white", height=1, text="清空所有代理地址", command=clearproxy).pack(
            pady=2)
        Button(left, font=("楷体", (15)), bg="black", fg="white", height=1, text="筛选优化代理", command=optimizeproxy).pack(
            pady=2)
        Button(left, font=("楷体", (15)), bg="black", fg="white", height=1, text="停止筛选优化代理",
               command=stopoptimizeproxy).pack(pady=2)
        Label(left, font=("楷体", (10)), text="筛选测试网站", bg="black", fg="white").pack(pady=2)
        texttestproxy = Entry(left)
        texttestproxy.pack(pady=2, padx=10)
        texttestproxy.insert(END, "http://www.baidu.com")
        Label(rightlist, font=("楷体", (12)), text="设置线程数.\n(线程越大下载\n图片速度越快，\n根据机器配置与\n网络情况设置，\n建议在100-1000之间)",
              bg="black", fg="white").pack(pady=2)
        textthread = Entry(rightlist, width=20)
        textthread.pack(pady=2, padx=10)
        textthread.insert(END, 10)
        Label(rightlist, font=("楷体", (15)), bg="black", fg="white", height=1, text="已有项目列表").pack(pady=2)
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
        b0 = Button(rightlist, font=("楷体", (15)), bg="black", fg="white", height=1, text="使用项目", command=openproject)
        b0.pack(pady=2)
        Checkbutton(rightlist, font=("楷体", (10)),
                    text="使用代理\n(部分网站有反爬功能\n设置代理可防止被封IP)", bg="black", fg="red",
                    variable=checkv).pack(pady=2)
        Label(rightlist, font=("楷体", (15)), bg="black", fg="white", height=1, text="扫描模式", ).pack(pady=2)
        radiov = IntVar()
        Radiobutton(rightlist, font=("楷体", (10)), text="只扫描此地址", bg="black", fg="yellow"
                    , variable=radiov, value=0).pack(pady=2, anchor=W)
        Radiobutton(rightlist, font=("楷体", (10)), text="只扫描此网站内", bg="black", fg="yellow"
                    , variable=radiov, value=1).pack(pady=2, anchor=W)
        Radiobutton(rightlist, font=("楷体", (10)), text="全网扫描\n(百度模式扫描，\n以设置的网址为根地址)"
                    , variable=radiov, value=2, bg="black", fg="yellow").pack(pady=2, anchor=W)
        Label(left, font=("楷体", (10)), text="版本信息:\n"
                                            "版本.0.1test\n"
                                            "用于学习Pthon编码\n"
                                            "特性的手工无框架版\n"
                                            "网站图片爬虫。\n"
                                            "出品人:MR.ZHOU.\n"
                                            "邮箱:542945190@qq.com", bg="black", fg="white").pack(pady=2)
        Button(left, font=("楷体", (15)), bg="black", fg="red", height=1, text="配置数据库", command=setmysql).pack(pady=2,
                                                                                                             anchor=S)

        return rootwindow

    def mysqlconnectwindow(self):
        """
        创建数据库窗口
        :return:
        """
        labletext = SQLCONNECTTEXT_CN
        sqlwin = Tk()
        sql=Mysql()
        # sqlwin.resizable(width=False, height=False)
        sqlwin.configure(background="black")
        sqlwin.geometry("460x500+100+100")
        ##################################################################################################
        top = Frame(sqlwin, width=300, height=50, bg="black")
        top.place(x=20, y=0)
        left = Frame(sqlwin, width=100, height=500, bg="black", )
        left.place(x=0, y=50)
        rigth = Frame(sqlwin, width=300, height=500, bg="black", )
        rigth.place(x=250, y=55)
        bottom = Frame(sqlwin, width=300, height=50, bg="black", )
        bottom.place(x=200, y=450)
        ##################################################################################################
        Label(top, font=("楷体", (15)), bg="black", fg="white", text="创建数据库，请确认已经正确安装mysql数据库！").pack(side=TOP)
        for lable in labletext:
            Label(left, font=("楷体", (15)), bg="black", fg="white", text=lable).pack(pady=19, anchor=E)
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
        user.insert(END, "root")
        db.insert(tkinter.END, "superimage")
        prot.insert(tkinter.END, "3306")
        charset.insert(tkinter.END, "utf8")

        def cmd():
            result = sql.createsql(dbhost=host.get(), dbname=db.get(), dbuser=user.get(),
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



class Mysql():
    def __init__(self):
        self.info = ""
        self.sqllink = False
        self.cursor = None
        self.db = None
    def linksql(self):
        try:
            dbinfo = open("./dbinfo.txt"  , "r")
            dbi = dbinfo.readlines()
            dbinfo.close()
            self.dbconfig = {
                "host": dbi[0].strip("\n"),
                "user": dbi[2].strip("\n"),
                "passwd": dbi[3].strip("\n"),
                "port": int(dbi[4].strip("\n")),
                "charset": dbi[5].strip("\n"),
                "db": dbi[1].strip("\n")
            }
            try:
                self.db = pymysql.connect(**self.dbconfig)
                print("数据库连接成功")
                self.info = ("数据库连接成功")
                self.cursor = self.db.cursor()
                self.sqllink = True
            except Exception as error:
                print("数据库连接失败错误:%s" % error)
                self.info = ("数据库连接失败错误:%s" % error)
                self.sqllink = False
        except Exception as error:
            print("请先创建数据库")
            self.info = ("请先创建数据库")
    def readurl(self,projectname,urlid):
        try:
            self.linksql()
            sqlcommand = ("SELECT * FROM %s WHERE id = %d" % ((projectname + "url"), urlid))
            self.cursor.execute(sqlcommand)
            self.db.commit()
            url = self.cursor.fetchone()
            self.db.close()
            return url
        except Exception as error:
            self.info="读取url失败%s"%error
            return None

    def createsql(self, dbhost="192.168.2.102", dbname="superimage", dbuser="root", dbpassword="woailijing",
                  dbport=3306,
                  charset="utf8"):
        # 创建数据库

        self.dbconfig = {
            "host": dbhost,
            "user": dbuser,
            "passwd": dbpassword,
            "port": dbport,
            "charset": charset,
        }
        try:
            self.db = pymysql.connect(**self.dbconfig)
            print("数据库 连接成功")
            self.info = ("数据库 连接成功")
            self.cursor = self.db.cursor()
            # 创建数据库
            try:
                sqlcommand = "create database %s  " % dbname
                self.cursor.execute(sqlcommand)
                print("创建数据库成功")
                self.info = ("创建数据库成功")
                self.db.close()
                return True
            except Exception as error:
                self.db.close()
                print("已有此数据库或创建数据库失败%s" % error)
                self.info = ("已有此数据库或创建数据库失败%s" % error)
                result = "已有此数据库或创建数据库失败%s" % error
                return result
        except Exception as error:
            print("数据库连接失败错误:%s" % error)
            self.info = ("数据库连接失败错误:%s" % error)
            result = "数据库连接失败错误:%s" % error
            return result

    def createproject(self, projectname):
        # 创建项目
        # 项目表
        project = {
            "projectname": projectname,
            "id": "id",
            "url": "url",
            "urldata": "urldata",
            "imagepath": "imagepath"
        }
        try:
            self.linksql()
            sql = "create table %s(%s int(20) primary key AUTO_INCREMENT,%s char(200) ,%s MediumText ,%s char(100))default charset=utf8" \
                  % ((project["projectname"] + "data"), project["id"], project["url"], project["urldata"],
                     project["imagepath"]
                     )
            self.cursor.execute(sql)
            sql = "create table %s(%s int(20) ,%s char(200) primary key)default charset=utf8" \
                  % ((project["projectname"] + "url"), project["id"], project["url"])
            self.cursor.execute(sql)
            print("项目数据表创建成功")
            self.info = ("项目数据表创建成功")
            self.db.close()
        except Exception as error:
            self.db.close()
            print("已存在项目数据表或项目名错误创建项目失败%s" % error)
            self.info = ("已存在项目数据表或项目名错误创建项目失败%s" % error)

    def inputimagepath(self, url, path, projectname):
        try:
            self.linksql()
            sql = r"insert into %s(url,imagepath) values('%s','%s')" % ((projectname + "data"), url, path)
            self.cursor.execute(sql)
            self.db.commit()
            print("图片路径%s写入数据库成功" % (path))
            self.info = ("图片路径%s写入数据库成功" % (path))
            self.db.close()
            return True
        except Exception as error:
            self.db.close()
            self.db.rollback()
            print("图片%s路径写入数据库失败已滚回,错误：%s" % (path, error))
            self.info = ("图片%s路径写入数据库失败已滚回,错误：%s" % (path, error))
            return False

    def inputtextdata(self, url, projectname, textdata):
        """
         #尝试将下载url的数据保存到数据库。
        :param url:
        :param projectname: 数据库表名
        :return:
        """
        try:
            self.linksql()
            textdata = self.db.escape_string(textdata)
            sql = r"insert into %s(url,urldata) values('%s','%s')" % (
                (projectname + "data"), url, textdata)
            self.cursor.execute(sql)
            self.db.commit()
            print("数据%s写入数据库成功" % url)
            self.info = ("数据%s写入数据库成功" % url)
            self.db.close()
            return True
        except Exception as error:  
            self.db.rollback()
            self.db.close()
            print("数据%s写入数据库失败.....已滚回,错误：%s" % (url, error))
            self.info = ("数据%s写入数据库失败.....已滚回,错误：%s" % (url, error))
            return False
    def inputurl(self, projectname, id, url):
        """
        用于保存过滤后的url地址
        :param projectname:
        :param id:
        :param url:
        :return:
        """
        try:
            self.linksql()
            url = self.db.escape_string(url)
            sql = "insert into %s(id,url) values(%s,'%s')" % ((projectname + "url"), id, url)
            self.cursor.execute(sql)
            self.db.commit()
            print("url%s写入数据库成功" % url)
            self.info = ("url%s写入数据库成功" % url)
            self.db.close()
            return True
        except Exception as error:
            self.db.rollback()
            self.db.close()
            print("url%s写入数据库失败%s" % (url, error))
            self.info = ("url%s写入数据库失败%s" % (url, error))
    def testsql(self):
        pass
    def delproject(self, projectname):
        try:
            self.linksql()
            self.cursor.execute(r"drop table %s" % (projectname + "data"))
            self.cursor.execute(r"drop table %s" % (projectname + "url"))
            print("项目数据表删除成功")
            self.info = ("项目数据表删除成功")
            self.db.close()
        except Exception as error:
            self.db.close()
            print("不存在此项目数据表或删除失败%s" % error)
            self.info = ("不存在此项目数据表或删除失败%s" % error)
if __name__ == '__main__':
    s = TKwindow().rootwindow()
    sql = Mysql()
    sql.linksql()
    s.mainloop()
"pyinstaller -D ./exe/exetest.py"