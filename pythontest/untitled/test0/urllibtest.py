import urllib.request



urltext = urllib.request.urlopen("http://588ku.com/")
textdata = urltext.read()
textdata= textdata.decode("utf8")
print(textdata)
