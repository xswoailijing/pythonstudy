import pymysql
import os
import urllib.request
"""
用于链接mysql数据库，保存图片路径和过滤到的url信息.

"""
class mysql():
    def __init__(self):
        self.info=""
        self.sqllink = False
        self.cursor=None
        self.db=None
    def linksql(self):
        try:
            dbinfo = open("%s"%os.sys.path[0]+"/dbinfo.txt", "r")
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
                self.info=("数据库连接成功")
                self.cursor = self.db.cursor()
                self.sqllink = True
            except Exception as error:
                print("数据库连接失败错误:%s" % error)
                self.info=("数据库连接失败错误:%s" % error)
                self.sqllink = False
        except Exception as error:
            print("请先创建数据库")
            self.info=("请先创建数据库")


    def createsql(self,dbhost="192.168.2.102", dbname="superimage", dbuser="root", dbpassword="password", dbport=3306,
                 charset="utf8"):
        #连接数据库

        self.dbconfig = {
            "host": dbhost,
            "user": dbuser,
            "passwd": dbpassword,
            "port": dbport,
            "charset": charset,
        }
        try:
            self.db = pymysql.connect(**self.dbconfig)
            print("数据库连接成功")
            self.info=("数据库连接成功")
            self.cursor = self.db.cursor()
            # 创建数据库
            try:
                sqlcommand = "create database %s  " % dbname
                self.cursor.execute(sqlcommand)
                print("创建数据库成功")
                self.info=("创建数据库成功")
                return True
            except Exception as error:
                print("已有此数据库或创建数据库失败%s" % error)
                self.info=("已有此数据库或创建数据库失败%s" % error)
                result = "已有此数据库或创建数据库失败%s" % error
                return result
        except Exception as error:
            print("数据库连接失败错误:%s" % error)
            self.info=("数据库连接失败错误:%s" % error)
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
            sql = "create table %s(%s int(20) primary key AUTO_INCREMENT,%s char(200) ,%s MediumText ,%s char(100))default charset=utf8" \
                  % ((project["projectname"] + "data"), project["id"], project["url"], project["urldata"],
                     project["imagepath"]
                     )
            self.cursor.execute(sql)
            sql = "create table %s(%s int(20) ,%s char(200) primary key)default charset=utf8" \
                  % ((project["projectname"] + "url"), project["id"], project["url"])
            self.cursor.execute(sql)
            print("项目数据表创建成功")
            self.info=("项目数据表创建成功")
        except Exception as error:
            print("已存在项目数据表或项目名错误创建项目失败%s" % error)
            self.info=("已存在项目数据表或项目名错误创建项目失败%s" % error)

    def inputimagepath(self, url,path, projectname):
        try:
            sql = r"insert into %s(url,imagepath) values('%s','%s')" % ((projectname+"data"), url, path)
            self.cursor.execute(sql)
            self.db.commit()
            print("图片路径%s写入数据库成功" % (path))
            self.info=("图片路径%s写入数据库成功" % (path))
            return True
        except Exception as error:
            self.db.rollback()
            print("图片%s路径写入数据库失败已滚回,错误：%s" % (path, error))
            self.info=("图片%s路径写入数据库失败已滚回,错误：%s" % (path, error))
            return False
    def inputtextdata(self, url,projectname, textdata):
        """
         #尝试将下载url的数据保存到数据库。
        :param url:
        :param projectname: 数据库表名
        :return:
        """
        textdata = self.db.escape_string(textdata)
        try:
            sql = r"insert into %s(url,urldata) values('%s','%s')" % (
                (projectname + "data"),url, textdata)
            self.cursor.execute(sql)
            self.db.commit()
            print("数据%s写入数据库成功" % url)
            self.info=("数据%s写入数据库成功" % url)
            return True
        except Exception as error:
            self.db.rollback()
            print("数据%s写入数据库失败.....已滚回,错误：%s" % (url, error))
            self.info=("数据%s写入数据库失败.....已滚回,错误：%s" % (url, error))
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
            url=self.db.escape_string(url)
            sql = "insert into %s(id,url) values(%s,'%s')" % ((projectname+"url"), id, url)
            self.cursor.execute(sql)
            self.db.commit()
            print("url%s写入数据库成功" % url)
            self.info=("url%s写入数据库成功" % url)
            return True
        except Exception as error:
            print("url%s写入数据库失败%s" % (url, error))
            self.info=("url%s写入数据库失败%s" % (url, error))
    def testsql(self):
        pass

    def delproject(self, projectname):
        try:
            self.cursor.execute(r"drop table %s" % (projectname + "data"))
            self.cursor.execute(r"drop table %s" % (projectname + "url"))
            print("项目数据表删除成功")
            self.info=("项目数据表删除成功")
        except Exception as error:
            self.db.close()
            print("不存在此项目数据表或删除失败%s" % error)
            self.info=("不存在此项目数据表或删除失败%s" % error)
        pass


if __name__ == '__main__':
    projectname = "23data"
    s = mysql()
    s.linksql()
    # s.createsql()
    # s.createproject(projectname)
    # s.delproject("acfunall")
    urltext = urllib.request.urlopen("http://588ku.com")
    textdata = urltext.read()
    print(textdata)
    textdata = textdata.decode("utf8")
    print(textdata)
    url = "123"
    textdata = s.db.escape_string(textdata)
    url= s.db.escape_string(url)

    sql = r"insert into %s(url,urldata) values ('%s','%s')" % (projectname, url, textdata)
    s.cursor.execute(sql)
    s.db.commit()
