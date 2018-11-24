
from pymongo import MongoClient


conn=MongoClient("192.168.2.102",27017)

db = conn.mongo  #连接mydb数据库，没有则自动创建
db.authenticate("root", "woailijing") #默认的MongoDB没有用户验证MongoDB是以key value hashid的方式保存数据。

my_set = db.mongotest
#插入数据
# my_set.insert({"name":"zhangsan","age":18})
#添加多条数据到集合中
users=[{"name":"zhangsan","age":18},{"name":"lisi","age":20}]
my_set.insert(users)
#或

#查询全部
# for i in my_set.find():
#     print(i)
#查询name=zhangsan的
for i in my_set.find({"name":"zhangsan"}):
    print(i)
# print(my_set.find_one({"name":"zhangsan"}))
my_set.remove()