import hashlib

f=open("./cj.jpg","rb")
md5=hashlib.md5(f.read())

print(md5.hexdigest())