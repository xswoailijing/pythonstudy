import feiji
import zidan
import config
import pygame
import time
import random


class feijigame(pygame.sprite.Sprite):
    # 初始化游戏
    def __init__(self):
        super().__init__()

        self.wojunzidanjishi = time.time()
        self.dijunzidanjishi = time.time()
        self.chushidijishu = config.DIJISHULIANG
        self.dijiid = []
        self.dijibaozhashu = 0
        self.dijizongshu = 0
        self.zidanid = []
        self.zidanzongshu = 0
        self.dijizidanid = []
        self.dijizidanzongshu = 0
        self.wojiid = []
        self.wojibianhao = 0

        self.name = globals()

        self.breke1 = pygame.image.load(config.BERKE)
        self.nadu = 1
        self.key = 1

    def startgame(self, nandu=1):

        # 加载窗口
        pygame.init()
        game = pygame.display.set_mode(config.WINDOWS)

        # 加载飞机
        self.__jiazaifeiji()

        # 游戏循环
        while True:

            # 渲染背景
            game.blit(self.breke1, (0, 0))
            # 事件监听
            self.__jianting(game)

            # 爆炸测试

            # 碰撞检测
            self.pengzhuangjiance(game)

            # 遍历敌机与敌机子弹位置
            for dijiid in self.dijiid:
                self.name["feijitest%s" % dijiid].feixing(game)
            for dijizidan in self.dijizidanid:
                self.name["dijizidan%s" % dijizidan].feixing(game)

            # 遍历我机与子弹位置
            for zidanid in self.zidanid:
                self.name["zidan%s" % zidanid].zidanfeixing(game)
            for wojiid in self.wojiid:
                self.name["wojiid%s" % wojiid].xianshi(game)

            # 整体渲染

            # 设置fps
            clock = pygame.time.Clock()
            clock.tick(config.FPS)
            pygame.display.update()

            # 判断游戏是否退出

            self.__gameexit()

    def __jiazaifeiji(self):

        # 加载敌机
        while len(self.dijiid) <= self.chushidijishu:
            self.dijizongshu += 1
            self.dijiid.append(self.dijizongshu)
            self.name["feijitest%s" % self.dijizongshu] = feiji.dijunfeiji()

            # 加载我机

        self.name["wojiid%s" % self.wojibianhao] = feiji.wojunfeiji()
        self.wojiid.append(0)
        self.wojibianhao += 1

    def __jiazaizidan(self, game):
        # 加载子弹
        # 加载我机子弹
        for wojiid in self.wojiid:
            zidanweizhi = self.name["wojiid%s" % wojiid].weizhi
            zidanfangxiang = self.key
            self.zidanzongshu += 1
            self.zidanid.append(self.zidanzongshu)
            self.name["zidan%s" % self.zidanzongshu] = zidan.zidan((zidanweizhi.x + 10, zidanweizhi.y + 5),
                                                                   zidanfangxiang)

    def __jianting(self, game):
        # 监听时钟

        # 加载敌机子弹
        if time.time() > self.dijunzidanjishi + 0.2 and len(self.dijiid) > 0:
            dijiid = random.choice(self.dijiid)
            self.dijizidanid.append(self.dijizidanzongshu)
            self.name["dijizidan%s" % self.dijizidanzongshu] = \
                zidan.dijizidan(
                    (self.name["feijitest%s" % dijiid].weizhi.x, self.name["feijitest%s" % dijiid].weizhi.y),
                    self.name["feijitest%s" % dijiid].fangxiang)
            self.dijizidanzongshu += 1
            self.dijunzidanjishi = time.time()

        # 事件监听
        for event in pygame.event.get():
            pass
        # 监听键盘
        key = pygame.key.get_pressed()
        for wojiid in self.wojiid:
            if key[pygame.K_d]:
                self.key = 4
                self.name["wojiid%s" % wojiid].feixing(self.key, game)
            if key[pygame.K_a]:
                self.key = 3
                self.name["wojiid%s" % wojiid].feixing(self.key, game)
            if key[pygame.K_w]:
                self.key = 1
                self.name["wojiid%s" % wojiid].feixing(self.key, game)
            if key[pygame.K_s]:
                self.key = 2
                self.name["wojiid%s" % wojiid].feixing(self.key, game)
            if key[pygame.K_SPACE]:

                if float(time.time()) > float(self.wojunzidanjishi) + config.ZIDANFASHEPINGLV:
                    self.__jiazaizidan(game)
                    self.wojunzidanjishi = time.time()
            # 双人游戏键盘监听，缺省
            if key[pygame.K_RIGHT]:
                self.key = 8
                self.name["wojiid%s" % wojiid].feixing(self.key, game)
            if key[pygame.K_LEFT]:
                self.key = 7
                self.name["wojiid%s" % wojiid].feixing(self.key, game)
            if key[pygame.K_UP]:
                self.key = 5
                self.name["wojiid%s" % wojiid].feixing(self.key, game)
            if key[pygame.K_DOWN]:
                self.key = 6
                self.name["wojiid%s" % wojiid].feixing(self.key, game)
            if key[pygame.K_0]:

                if float(time.time()) > float(self.wojunzidanjishi) + config.ZIDANFASHEPINGLV:
                    self.__jiazaizidan(game)
                    self.wojunzidanjishi = time.time()

    def pengzhuangjiance(self, game):

        # 敌机检测击中
        for dijiid in self.dijiid:
            for zidanid in self.zidanid:
                dijiweizhi = self.name["feijitest%s" % dijiid].weizhi
                zidanweizhi = self.name["zidan%s" % zidanid].zidanweizhi
                if dijiweizhi.x + dijiweizhi.width >= zidanweizhi.x and \
                        dijiweizhi.x <= zidanweizhi.x + zidanweizhi.width and \
                        dijiweizhi.y + dijiweizhi.height >= zidanweizhi.y and \
                        dijiweizhi.y <= zidanweizhi.y + zidanweizhi.height:
                    self.name["feijitest%s" % dijiid].dijibaozha(game)
                    self.dijiid.remove(dijiid)
                    del self.name["feijitest%s" % dijiid]
                    self.name["zidan%s" % zidanid].zi(game)
                    self.zidanid.remove(zidanid)
                    del self.name["zidan%s" % zidanid]
                    break

            # 我检测击中
            for dijizidanid in self.dijizidanid:
                for wojiid in self.wojiid:
                    dijiweizhi = self.name["dijizidan%s" % dijizidanid].zidanweizhi
                    if dijiweizhi.x + dijiweizhi.width >= self.name["wojiid%s" % wojiid].weizhi.x and \
                            dijiweizhi.x <= self.name["wojiid%s" % wojiid].weizhi.x + self.name[
                        "wojiid%s" % wojiid].weizhi.width and \
                            dijiweizhi.y + dijiweizhi.height >= self.name["wojiid%s" % wojiid].weizhi.y and \
                            dijiweizhi.y <= self.name["wojiid%s" % wojiid].weizhi.y + self.name[
                        "wojiid%s" % wojiid].weizhi.height:

                        self.name["dijizidan%s" % dijizidanid].baozha(game)
                        self.dijizidanid.remove(dijizidanid)
                        del self.name["dijizidan%s" % dijizidanid]
                        self.name["wojiid%s" % wojiid].zhongdan(game)
                        if self.name["wojiid%s" % wojiid].hp <= 0:
                            self.wojiid.remove(wojiid)
                            del self.name["wojiid%s" % wojiid]
                            print("游戏结束...")
                            break

            # 我机检测碰撞
        for dijiid in self.dijiid:
            for wojiid in self.wojiid:
                dijiweizhi = self.name["feijitest%s" % dijiid].weizhi
                if dijiweizhi.x + dijiweizhi.width >= self.name["wojiid%s" % wojiid].weizhi.x and \
                        dijiweizhi.x <= self.name["wojiid%s" % wojiid].weizhi.x + self.name[
                    "wojiid%s" % wojiid].weizhi.width and \
                        dijiweizhi.y + dijiweizhi.height >= self.name["wojiid%s" % wojiid].weizhi.y and \
                        dijiweizhi.y <= self.name["wojiid%s" % wojiid].weizhi.y + self.name[
                    "wojiid%s" % wojiid].weizhi.height:

                    self.name["feijitest%s" % dijiid].dijibaozha(game)
                    self.dijiid.remove(dijiid)
                    del self.name["feijitest%s" % dijiid]
                    self.name["wojiid%s" % wojiid].zhongdan(game)
                    if self.name["wojiid%s" % wojiid].hp <= 0:
                        self.wojiid.remove(wojiid)
                        del self.name["wojiid%s" % wojiid]
                        print("游戏结束...")
                        break

    def __gameexit(self):
        # 判断是否退出游戏，没有这个循环在window下窗口会假死.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


def main():
    feiji = feijigame()
    feiji.startgame(1)


if __name__ == "__main__":
    main()
