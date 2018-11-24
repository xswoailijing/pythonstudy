
class filtration():
    def guolvtext(self):
        # 过滤爬取的文本文件
        pass

    def guolvimage(self, search):
        with open(self.dir + "/scanset.txt", "r") as f:
            starti = int(f.readline())
            endi = int(f.readline())
            line = int(f.readline())
            imagestarti = int(f.readline())
            imageendi = int(f.readline())
            opentimeout = int(f.readline())
            retry = int(f.readline())
            opencoding = f.readline()
            coding = f.readline()
            f.close()
        self.dirfile = self.dir + "/urldata.txt"
        with open(self.dirfile, "r", encoding=coding) as urlfile:
            # 设置上次过滤到的行
            urlfile.seek(line)
            while imagestarti < imageendi:
                urlf = urlfile.readline()
                if len(urlf) == 0:
                    urlfile.close()
                    print("%s全部过滤完成，共%s张图片" % (self.dirfile, imagestarti))
                    return
                else:
                    r = re.search(search, urlf)
                    line += 1
                    with open(self.dir + "/scanset.txt", "r") as f:
                        fileline = f.readlines()
                        f.close()
                        fileline[2] = "%s\n" % line
                    with open(self.dir + "/scanset.txt", "w") as f:
                        for i in fileline:
                            f.write("%s" % i)
                        f.close()
                    if r is not None:
                        url = r.group()
                        do = 0
                        while do < 3:
                            proxy.proxystart().proxystart(pachong1.proxyiplist)
                            dump = openurltofile.openurltofile().imagedownload(self.dir + "/" + "%s.jpg" % imagestarti, url,
                                                                               opentimeout)
                            if dump == True:
                                imagestarti += 1
                                with open(self.dir + "/scanset.txt", "r") as f:
                                    fileline = f.readlines()
                                    f.close()
                                    fileline[3] = "%s\n" % imagestarti
                                with open(self.dir + "/scanset.txt", "w") as f:
                                    for i in fileline:
                                        f.write("%s" % i)
                                    f.close()
                                    print("已过滤%s张图片" % imagestarti)
                                    print("已过滤到文件的%s行" % line)
                                break




