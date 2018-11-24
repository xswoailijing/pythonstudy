import urllib.request
import json
import requests




url="http://61.135.217.7:80"
r = requests.get(url)

print(r.elapsed)
print(r.elapsed.total_seconds())
print(r.elapsed.microseconds)


r = requests.get(url)
if r.elapsed.total_seconds() > 1:
    print("连接%s时延迟大于%s秒" % (url, 1))
else:
    print("连接到%s时延迟小于%s秒" % (url, 1))

# url = ("http://%s" % self.testproxyip)
try:
    r = requests.get(url)
    if r.elapsed.seconds() > 1:
        print("连接%s时延迟大于%s秒" % (url, 1))
    else:
        print("连接到%s时延迟小于%s秒" % (url, 1))

except:
    print("不能连接到%s" % url)
# r=urllib.request.urlopen(url)
# # r2=urllib.request.addinfourl(headers="")
# time=r.elapsed.microseconds()
# print(time)
#
# r1=r.read()
# r1=r1.decode("utf8")
# f=open("./info.txt","w",encoding="utf8")
#
# f.writelines(r1)
# f.close()
#
# print(r1)