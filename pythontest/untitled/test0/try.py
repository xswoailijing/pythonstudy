# a=0
# try:
#     a = int((input("请输入整数")))
#
#
#
# except Exception as result:
#     print("未知错误：%s"%result)
# else:
#     print("成功执行次数加一。")
# finally:
#     print("执行次数加一。")
# print(a)
# # except:
# #     print("输入错误")
# # except:
# #     print("输入错误2")

def inputpasswd():
    a = (input("请输入小于8位整数"))
    if len(a) < 8:
        print("成功")
        return a

    excep = Exception("过长")
    raise excep


print(inputpasswd())
