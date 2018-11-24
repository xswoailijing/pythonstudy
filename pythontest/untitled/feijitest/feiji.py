import pygame
import config
import random

#敌机类
class dijunfeiji(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.s = config.DIJISEEPS
        self.feixingjuli = config.DIJIFEIXINGJULI
        self.hp = config.DIJIHP
        r = random.randint(1, 4)
        if r == 1:
            config.DIJIWEIZHI = ((random.randint(0, config.WINDOWS[0] - config.DIJIWEIZHI[1][1]), 0),
                                 (config.DIJIWEIZHI[1]))
        elif r == 2:
            config.DIJIWEIZHI = (
                (random.randint(0, config.WINDOWS[0]), config.WINDOWS[1] - config.DIJIWEIZHI[1][1]),
                (config.DIJIWEIZHI[1]))
        elif r == 3:
            config.DIJIWEIZHI = ((0, random.randint(0, config.WINDOWS[1] - config.DIJIWEIZHI[1][1])),
                                 (config.DIJIWEIZHI[1]))
        else:
            config.DIJIWEIZHI = (
                (config.WINDOWS[0], random.randint(0, config.WINDOWS[1] - config.DIJIWEIZHI[1][1])),
                (config.DIJIWEIZHI[1]))
        self.weizhi = pygame.Rect(config.DIJIWEIZHI)
        self.window = config.WINDOWS
        self.fangxiang = config.DIJIFANGXIANG
        self.fangxiangr = pygame.image.load(config.DIJIWAIGUANR)
        self.fangxiangl = pygame.image.load(config.DIJIWAIGUANL)
        self.fangxiangup = pygame.image.load(config.DIJIWAIGUANUP)
        self.fangxiangdown = pygame.image.load(config.DIJIWAIGUANDOWN)
        self.baozha = pygame.image.load(config.DIJIBAOZHA)
        # self.zhongdan=pygame.image.load(config.DIJIZHONGDAN)

    def feixing(self, game):

        up = 1
        down = 2
        left = 3
        right = 4

        if self.feixingjuli <= 0:
            self.fangxiang = random.randint(1, 4)
            self.feixingjuli = random.randint(1, 20)

        # 判断飞机是否超出窗口边界
        if self.weizhi.x <= 0:
            self.weizhi.x += 2
            self.feixingjuli = 0
        elif self.weizhi.x >= self.window[0] - self.weizhi.width:
            self.weizhi.x -= 2
            self.feixingjuli = 0
        elif self.weizhi.y <= 0:
            self.weizhi.y += 2
            self.feixingjuli = 0
        elif self.weizhi.y >= self.window[1] - self.weizhi.height:
            self.weizhi.y -= 2
            self.feixingjuli = 0
        else:

            # 飞机移动
            if self.fangxiang == right:
                self.weizhi.x += self.s

            elif self.fangxiang == left:
                self.weizhi.x -= self.s

            elif self.fangxiang == down:
                self.weizhi.y += self.s
                self.fangxiang = down
            elif self.fangxiang == up:
                self.weizhi.y -= self.s

            if self.fangxiang == right:
                game.blit(self.fangxiangr, (self.weizhi.x, self.weizhi.y))
            if self.fangxiang == left:
                game.blit(self.fangxiangl, (self.weizhi.x, self.weizhi.y))

            if self.fangxiang == up:
                game.blit(self.fangxiangup, (self.weizhi.x, self.weizhi.y))

            if self.fangxiang == down:
                game.blit(self.fangxiangdown, (self.weizhi.x, self.weizhi.y))

        self.feixingjuli -= 1
        return

    def sheji(self):

        pass

    def dijibaozha(self, game):
        game.blit(self.baozha, (self.weizhi.x, self.weizhi.y))
    def zhongdan(self, game):
        game.blit(self.zhongdan, (self.weizhi.x, self.weizhi.y))
        pass
    def __del__(self):
        pass




#我机类
class wojunfeiji(pygame.sprite.Sprite):
    def __init__(self, ):
        super().__init__()
        self.s = config.SEEPS
        self.hp = config.HP
        self.weizhi = pygame.Rect(config.WEIZHI)
        self.fangxiang = config.FANGXIANG
        self.window = config.WINDOWS
        self.fangxiangr = pygame.image.load(config.WAIGUANR)
        self.fangxiangl = pygame.image.load(config.WAIGUANL)
        self.fangxiangup = pygame.image.load(config.WAIGUANUP)
        self.fangxiangdown = pygame.image.load(config.WAIGUANDOWN)
        self.baozha = pygame.image.load(config.BAOZHA)
#        self.zhongdan=pygame.image.load(config.ZHONGDAN)

    def feixing(self, key, game):

        up = 1
        down = 2
        left = 3
        right = 4

        if self.weizhi.x <= 0:
            self.weizhi.x += 2

        elif self.weizhi.x >= self.window[0] - self.weizhi.width:
            self.weizhi.x -= 2

        elif self.weizhi.y <= 0:
            self.weizhi.y += 2

        elif self.weizhi.y >= self.window[1] - self.weizhi.height:
            self.weizhi.y -= 2

        else:
            if key == right:
                self.weizhi.x += self.s
                self.fangxiang = right
            elif key == left:
                self.weizhi.x -= self.s
                self.fangxiang = left
            elif key == down:
                self.weizhi.y += self.s
                self.fangxiang = down
            elif key == up:
                self.weizhi.y -= self.s
                self.fangxiang = up

        if self.fangxiang == right:
            game.blit(self.fangxiangr, (self.weizhi.x, self.weizhi.y))
        if self.fangxiang == left:
            game.blit(self.fangxiangl, (self.weizhi.x, self.weizhi.y))

        if self.fangxiang == up:
            game.blit(self.fangxiangup, (self.weizhi.x, self.weizhi.y))

        if self.fangxiang == down:
            game.blit(self.fangxiangdown, (self.weizhi.x, self.weizhi.y))

    def sheji(self, game):

        pass

    def zhongdan(self, game):

        self.hp -= 1
#        game.blit(self.zhongdan, (self.weizhi.x, self.weizhi.y))
        if self.hp <= 0:
            game.blit(self.baozha, (self.weizhi.x, self.weizhi.y))

            print("我机爆炸")

    def xianshi(self, game):
        u = 1
        d = 2
        r = 4
        l = 3

        if self.fangxiang == r:
            game.blit(self.fangxiangr, (self.weizhi.x, self.weizhi.y))
        if self.fangxiang == l:
            game.blit(self.fangxiangl, (self.weizhi.x, self.weizhi.y))

        if self.fangxiang == u:
            game.blit(self.fangxiangup, (self.weizhi.x, self.weizhi.y))

        if self.fangxiang == d:
            game.blit(self.fangxiangdown, (self.weizhi.x, self.weizhi.y))
