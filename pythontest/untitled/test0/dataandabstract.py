import time
from abc import abstractmethod,ABCMeta
# 抽象方法
def whi():
    i=0
    x=1
    t0=time.time()

    while i <10000:
       i+=1
       x=x+(i+x)
       print("%s\n"%x)
    t=(time.time()-t0)
    t=t*1000
    print("%s\n"%t)


class Payment(ABCMeta):  # 抽象类/接口类
    @abstractmethod  # 给接口类加装饰器
    def payment(self, money): pass


if __name__ == '__main__':
    whi()


