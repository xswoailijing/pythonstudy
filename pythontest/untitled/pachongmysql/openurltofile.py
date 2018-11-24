"""


#模块用于包含两个用于下载指定url的类。
提供两种下载方式，数据方式与bite方式。

"""

import urllib.request
import re
import hashlib
import os


class openurltofile():

    def __init__(self):
        self.info = []

        pass

    def imagedownload(self, projectname, type, url, timeout):
        try:
            image = urllib.request.urlopen(url, timeout=timeout)
            image1 = image.read()
            md5 = hashlib.md5(image1)
            md5 = md5.hexdigest()
            with open("%s/%s/%s%s" % (os.sys.path[0], projectname, md5, type), "wb") as f:
                f.write(image1)
                f.close()
                print("图片%s已下载且重命名为%s" % (url, "%s/%s/%s%s" % (os.sys.path[0], projectname, md5, type)))
                self.info = ("图片%s已下载且重命名为%s" % (url, "%s/%s/%s%s" % (os.sys.path[0], projectname, md5, type)))
                return "%s/%s/%s%s" % (os.sys.path[0], projectname, md5, type)
        except Exception as error:
            print("图片%s未能下载%s" % (url, error))
            self.info = ("图片%s未能下载%s" % (url, error))
            return False


if __name__ == '__main__':
    url = "https://bpic.588ku.com/illus_pic/18/09/28/d2c490db98564da3c3b79fda69dbe9ec.jpg"
    # pa=pachong.requesttools()
    # pa.setproxylistfile("./proxyiplist/runproxyurl.txt")
    # urllib.request.Request.add_header("123")
    # proxy.proxy().proxy(pa.proxyiplist)
    url = urllib.request.Request("http://ltaaa.com")
    op = urllib.request.urlopen(url)
    op = op.read().decode("gbk")
    # openurltofile().tupian("./1.jpg",url,timeout=5)
    op = re.findall(r"http[A-Za-z0-9._+/:\-]+", op)
    print(type(op))
    print(op)
    # d=gzip.decompress(d)
    # d=d.decode("utf8")
    # print(d)
    pass
