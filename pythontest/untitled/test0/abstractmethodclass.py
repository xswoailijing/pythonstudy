from abc import abstractmethod,ABCMeta
class Payment(metaclass=ABCMeta): #抽象类/接口类
    @abstractmethod            #给接口类加装饰器
    def payment(self,money):pass

class Applepay(Payment):
    def payment(self,money):
        print('苹果 支付了%d元'%money)
def payment(pay_obj,money):
    pay_obj.payment(money)

class Alipay(Payment):
    def payment(self,money):
        print('支付宝 支付了%d元'%money)
def payment(pay_obj,money):
    pay_obj.payment(money)


class We():
    def fuqian(self,money):
        print('微信支付了%d元'%money)


p=[We(),Alipay()]


p[0].fuqian(1)
p[1].payment(1)