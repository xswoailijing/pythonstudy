



import re

r=re.search(r'http[A-Za-z0-9._+/:\-]+.jpg','"href=http://588ku.com/yishuzi/0-pxnum-0-0-0-7-0-1.jpg"123123')
t=r.group()
try:
    t=t.index(".jpg")
except:

    print(t)
