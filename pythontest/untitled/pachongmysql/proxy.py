import urllib.request
import os
import random
import re
import time

"""
设置访问代理模块：
从代理列表中随机抽取1个ip地址字典作为代理ip地址

可用返回0，不可用返回1

属性proxyip显示当前使用的代理ip


"""


class proxy():
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
        file = open("%s/" % os.sys.path[0] + "proxyiplist/runproxyurl.txt", "w")
        file.writelines("")
        file.close()
        i = 0
        with open("%s/" % os.sys.path[0] + "proxyiplist/proxyip.txt", "r") as file:
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
                                with open("%s/" % os.sys.path[0] + "proxyiplist/runproxyurl.txt", "a") as filehttpw:
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
        with open("%s/" % os.sys.path[0] + "proxyiplist/runproxyurl.txt", "r") as file:
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
        with open("%s/proxyiplist/updataproxyip.txt" % os.sys.path[0], "r", encoding="utf8") as file:
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
                        addfile = open("%s/proxyiplist/proxyip.txt" % os.sys.path[0], "a")
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


if __name__ == '__main__':
    pass
