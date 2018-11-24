import urllib.request
import urllib.parse
import json
class youdaofanyi():
    def __init__(self):
        self.fanyineirong=""

    def fanyi(self,fangyineirong):
        self.fanyineirong=fangyineirong
        url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        # data={
        #
        #     "type": "AUTO",
        #     "i": self.fanyineirong,
        #     "doctype": "json",
        #     "xmlVersion": "1.6",
        #     "keyfrom": "fanyi.web",
        #     "ue":"UTF-8",
        #     "typoResult": "true"
        # }

        data1={
        "i": self.fanyineirong,
        "from":"AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1540657909775",
        "sign": "6d4f0778a723bc6b3ca0a58e3c132c95",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
        "typoResult": "false",
        }
        portdata=urllib.parse.urlencode(data1).encode("utf8")
        print(portdata)
        response=urllib.request.urlopen(url,portdata)
        r=response.read()
        print(r)
        r1=r.decode("utf8")
        print(r1)
        r1=json.loads(r1)
        print(r1)
        l=r1["translateResult"]
        l=l[0][0]
        l=l["tgt"]
        print(l)
        return l



if __name__=="__main__":

    youdao = youdaofanyi()

    youdao.fanyi("你好")




