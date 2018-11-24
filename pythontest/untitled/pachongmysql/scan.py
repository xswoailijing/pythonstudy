import openurltofile
import urllib.request
import os
import re
import mysql
import proxy
import threading
class scan(object):
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
        imagedownload1 = openurltofile.openurltofile()
        # 读取配置文件
        f=open("%s/%s/scanset.txt"% (os.sys.path[0],projectname), "r")
        configlist =f.readlines()
        f.close()
        timeout=int(configlist[6].strip("\n"))
        # 测试根网址
        try:
            urllib.request.urlopen(configlist[9].strip("\n"))
        except Exception as error:
            print("根网页%s无法打开%s" % (configlist[9].strip("\n"), error))
            self.info.append("根网页%s无法打开%s" % (configlist[9].strip("\n"), error))
            return "根网页%s无法打开%s" % (configlist[9].strip("\n"), error)
        # 判断是否使用代理
        if proxy_set == True:
            proxyiplist =proxy.proxy().setproxylistfile()
        # 连接数据库
        try:
            sql = mysql.mysql()
            sql.linksql()
        except:
            return
       #初始化多线程参数
        sc=[]
        textdatautf8 = []
        textdatagbk = []
        th = []
        imaged=[]
        path=[]
        urldata=[]
        u=[]
        for i in range(0,thread):
            u.append(None)
            path.append(False)
            sc.append(True)
            textdatautf8.append(None)
            textdatagbk.append(None)
            th.append(True)
            imaged.append(False)
            #设置根网页地址
        u[0] = configlist[9].strip("\n")
        # 开始循环扫描
        while (int(configlist[0]) < int(configlist[1])) and \
                (int(configlist[3]) < int(configlist[4])) and \
                self.stop == False:
            # 多线程回调函数
            def scan(url, t):
                sc[t] = False
                self.info.append(proxy.proxy().proxystrat(proxyiplist))
                ########################################################################################################################
                try:
                    url.index(".jpg")
                    path[t] = imagedownload1.imagedownload(projectname, ".jpg", url,timeout)
                    imaged[t]=True
                    sc[t] = True
                    self.info.append(imagedownload1.info)
                    return
                except:
                    pass
                #########################################################################################################################
                try:
                    url.index(".gif")
                    path[t] = imagedownload1.imagedownload(projectname, ".gif", url,timeout)
                    imaged[t] = True
                    sc[t] = True
                    self.info.append(imagedownload1.info)
                    return
                except:
                    pass
                ##########################################################################################################################
                try:
                    url.index(".png")
                    path[t] = imagedownload1.imagedownload(projectname, ".png", url,timeout)
                    imaged[t] = True
                    sc[t] = True
                    self.info.append(imagedownload1.info)
                    return
                except:
                    pass
                #########################################################################################################################
                # 读取url数据
                try:
                    urltext = urllib.request.urlopen(u[i],timeout=3)
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
            i=0
            while i<thread:
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
                            print("网页%sutf8编码写入错误%s"%(u[i]),error)
                            self.info.append("网页%sutf8编码写入错误%s"%(u[i]),error)
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

                    if int(configlist[0]) < int(configlist[2]) :
                        sqlcommand = ("SELECT * FROM %s WHERE id = %d" % (
                            (projectname + "url"), int(configlist[0].strip("\n"))))
                        sql.cursor.execute(sqlcommand)
                        sql.db.commit()
                        url = sql.cursor.fetchone()
                        u[i] = url[1]
                        configlist[0] = "%s\n" % (int(configlist[0].strip("\n")) + 1)
                        print("已爬行%s个页面" % configlist[0].strip("\n"))
                        self.info.append("已爬行%s个页面" % configlist[0].strip("\n"))
                    th[i] = threading.Thread(target=scan, args=(u[i], i,))
                    th[i].setDaemon(True)
                    th[i].start()
                    i+=1
                    with open("%s/%s/scanset.txt" % (os.sys.path[0], projectname), "w+") as f:
                        for li in configlist:
                            f.write("%s" % li)
                        f.close()
            self.info=["0"]

if __name__ == '__main__':
    pass
    sc=scan()
    reurl = r"http[A-Za-z0-9._+/:\-]+"
    sc.allrun("585",reurl,thread=20)