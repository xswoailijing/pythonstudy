class renlei():
    renshu = 0

    @classmethod
    def miejue(cls):
        cls.renshu = 0
        print("人类灭绝")
        pass

    @classmethod
    def chongsheng(cls):
        cls.renshu = 1
        print("人类重生")

    @staticmethod
    def zhanting():
        print("pass")

    def __init__(self, tizhong=50, name="zhongguoren", shenggao=180,k=100):
        self.tizhong = tizhong
        self.name = name
        self.shenggao = shenggao
        self.k=k
        self.__yingsi = None
        renlei.renshu += 1

    def __yingsi(self):
        print("隐私")

    def chifan(self):
        print("吃饭")
        pass

    def paobu(self):
        print("跑步")
        pass

    def shuijiao(self):
        print("睡觉")
        self.__yingsi()

    def __str__(self):
        return "name:%s tizhong:%s" % (self.name, self.tizhong)


class xiaoming(renlei):

    def __init__(self, tizhong=50, name="zhongguoren", shenggao=180, jinbi=5):
        super().__init__()
        self.tizhong = tizhong
        self.name = name
        self.shenggao = shenggao
        self.__yingsi = None
        renlei.renshu += 1
        self.jinbi = jinbi

    def daren(self):
        print("打人")

    def chaojipao(self):
        super().paobu()
        print("超级跑")

    def chifan(self):
        print("小明吃法")

    def __del__(self):
        print("啊")


class xiaohong(xiaoming):

    def __init__(self, tizhong=50, name="zhongguoren", shenggao=180, yingbi=50):
        super().__init__()
        self.tizhong = tizhong
        self.name = name
        self.shenggao = shenggao
        self.__yingsi = None
        renlei.renshu += 1
        self.yingbi = yingbi

    def sharen(self):
        print("杀人")


class xiaojun(xiaohong):
    renshu = 1

    def __init__(self, tizhong=50, name="zhongguoren", shenggao=180, tongbi=500):
        super().__init__()
        self.tizhong = tizhong
        self.name = name
        self.shenggao = shenggao
        self.__yingsi = None
        renlei.renshu += 1
        self.tongbi = tongbi

    def chiren(self):
        print("吃人")


class feiren:
    pass

xiaojun1=xiaojun()
print(xiaojun1.k)