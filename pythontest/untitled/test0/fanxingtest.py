# python自动添加泛型。
import threading
list=[]
dict={}
tuple=()
list.append(1)
list.append("asdf")
list.append(threading.Thread())

print(type(list[1]))
print(type(list[0]))
print(type(list[2].start()))

print(isinstance(list,tuple))