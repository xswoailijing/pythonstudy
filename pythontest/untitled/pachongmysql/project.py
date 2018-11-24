import os
import scan
import mysql
"""
用于创建和删除项目目录，配置文件，与项目数据库表。

"""
class createprojact():
    def __init__(self):
        self.mysql = mysql.mysql()
        self.dir = "%s/" % os.sys.path[0]
    def createproject(self,url,projectname):
        # 创建项目
        if os.path.exists(self.dir + "/" + projectname):
            print("项目已经存在。")
            return True
        else:
            try:
                self.mysql.linksql()
                self.mysql.createproject(projectname)
                os.mkdir(self.dir + "/" + projectname)
                projectlist= open(self.dir + "/projectlist.txt", "a")
                projectlist.write(projectname+"\n")
                projectlist.close()
                config = open(self.dir + "/" + projectname + "/scanset.txt", "w")
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
        if os.path.exists(self.dir + "/" + projectname):
            try:
                listdir = os.listdir(self.dir + "/" + projectname)
                for l in listdir:
                    os.remove(self.dir + "/" + projectname + "/" + l)
                os.rmdir(self.dir + "/" + projectname)
                self.mysql.linksql()
                self.mysql.delproject(projectname)
                projectlist0= open(self.dir + "/projectlist.txt", "r")
                projectlist0.readlines()
                projectlist1 = open(self.dir + "/projectlist.txt", "w+")
                for l in projectlist0:
                    if l.strip("\n")!=projectname:
                        projectlist1.write(l+"\n")
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
if __name__ == "__main__":
    heads = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q = 0.9,"
                  " image/webp,image/apng,*/*;q = 0.8",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cache-Control": "max - age = 0",
        "Connection": "keep - alive",
        "Cookie":
            "Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac ="
            " 1788 * 1 * PC_VC;""smidV2 = 2018060717170535ac78b8fba601bae3a549f7c3ed8934005e3b5b64a"
            "619710;UN = qq_40759591;BT = 1532831414067;__utma = 17226283.677624927.1539056659.1539"
            "056659.1539056659.1;__utmz = 17226283.1539056659.1.1.utmcsr = baidu | utmccn = (organi"
            "c) | utmcmd = organic;c_adb = 1;ARK_ID = JS4baa15a386508c3f941b139c261337014baa;uui"
            "d_tt_dd = 10_28867322970 - 1540835084981 - 193890;dc_session_id = 10_1540835084981.6"
            "48263;UM_distinctid = 166c8615d0b105 - 024207c1a6db1b - 454c092b - 100200 - 166c8615"
            "d0c28d;Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac = 1540920038, 1540960065, 1540960106"
            ",1540961347;_ask_session = BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTM1MzkxYjhkYzFmNDNjOTFj"
            "YmI0NTQ5NTI0YTdkZDlhBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMThSSTRYcjdRV2ZoS2xTaHE1UDQ5V3A"
            "3dUJZSlhpQ3V3bG5GaFkwclRLd3c9BjsARg % 3D % 3D - -582ab15642fd601257814532953573ea044"
            "00343;dc_tos = phgcpx;Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac = 1540970854",

        "Host": "ask.csdn.net",
        "If-None-Match": 'W/"5682ee882575b8fd6edccb845515a0f1"',
        "Upgrade-Insecure - Requests": "1",
        "User-Agent": "Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/63.0.3239.132Safari/537.36"
    }

    # url = "http://www.ltaaa.com/"
    url = "http://www.tooopen.com/"
    # url = "http://588ku.com/"
    upproxyurl = "http://demo.docmobile.cn/http"
    testproxyurl = "https://www.baidu.com/"
    projectname = "tooopen"
    reurl = r"http[A-Za-z0-9._+/:\-]+"
    # url = urllib.request.Request(url,None,heads)
    pachong1 = createprojact()
    scan1=scan.scan()
    pachong1.createproject(url,projectname)
    # pachong1.delproject(projectname)
    scan.scan().allrun(projectname,reurl)

