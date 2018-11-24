"""最近需要对节点到源站自己做个监控，简单的ping可以检测到一些东西，但是http请求的检查也要进行，于是就研究了下pycurl
pycurl是个用c语言实现的python
库，虽然据说不是那么pythonic，但是却很高效，它支持的协议居多：

supporting
FTP, FTPS, HTTP, HTTPS, GOPHER, TELNET, DICT, FILE
andLDAP.libcurl
supports
HTTPS
certificates, HTTP
POST, HTTP
PUT, FTPuploading, kerberos, HTTP
form
based
upload, proxies, cookies, user + password
authentication, file
transfer
resume, http
proxytunneling and more!

这一堆协议已经很多了，我需要就是http一个，相对urlib来说，这个库可能更快些。

以下这个脚本是对某一个给定的url进行检查，并打印出http相应码，响应大小，建立连接时间，准备传输时间，传输第一个字节时间，完成时间
"""

# !/usr/bin/python
# coding: UTF-8
import pycurl
import sys


class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf


def test_gzip(input_url):
    t = Test()
    #gzip_test= open("gzip_test.txt", 'w')
    c = pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION, t.body_callback)
    c.setopt(pycurl.ENCODING, 'gzip')
    c.setopt(pycurl.URL, input_url)
    c.perform()
    http_code = c.getinfo(pycurl.HTTP_CODE)
    http_conn_time = c.getinfo(pycurl.CONNECT_TIME)
    http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)
    http_start_tran = c.getinfo(pycurl.STARTTRANSFER_TIME)
    http_total_time = c.getinfo(pycurl.TOTAL_TIME)
    http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)
    print
    'http_codehttp_size conn_time pre_tran start_tran total_time'
    print
    "%d%d %f %f %f %f" % (http_code, http_size, http_conn_time, http_pre_tran, http_start_tran, http_total_time)


if __name__ == '__main__':
    input_url = sys.argv[1]
    test_gzip(input_url)



"""
脚本运行效果

xu: ~ / curl$python
pycurl_test.py
http: // daxuxu.info /
http_code
http_size
conn_time
pre_tran
start_trantotal_time
200
8703
0.748147
0.748170
1.632642
1.636552
"""
