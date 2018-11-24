import config
import pygame

#我机子弹类
class zidan(pygame.sprite.Sprite):


    def __init__(self, zidanweizhi, zidanfangxiang):
        super().__init__()
        self.zidansudu = config.ZIDANSEEPS
        self.zidantiji = config.ZIDANTIJI
        self.zidanat = config.ZIDANWEILI
        self.zidanfangxiang = zidanfangxiang
        self.zidanweizhi = pygame.Rect(zidanweizhi ,config.ZIDANTIJI)
        self.zidanwaixingr = pygame.image.load(config.ZIDANWAIGUANR)
        self.zidanwaixingl = pygame.image.load(config.ZIDANWAIGUANL)
        self.zidanwaixingu = pygame.image.load(config.ZIDANWAIGUANU)
        self.zidanwaixingd = pygame.image.load(config.ZIDANWAIGUAND)
        self.zidanbaozha = pygame.image.load(config.ZIDANBAOZHA)

    def zidanfeixing(self, game):
        if self.zidanfangxiang == 1:
            self.zidanweizhi.y -= self.zidansudu
            game.blit(self.zidanwaixingu, (self.zidanweizhi.x, self.zidanweizhi.y))
        if self.zidanfangxiang == 2:
            self.zidanweizhi.y += self.zidansudu
            game.blit(self.zidanwaixingd, (self.zidanweizhi.x, self.zidanweizhi.y))
        if self.zidanfangxiang == 3:
            self.zidanweizhi.x -= self.zidansudu
            game.blit(self.zidanwaixingl, (self.zidanweizhi.x, self.zidanweizhi.y))
        if self.zidanfangxiang == 4:
            self.zidanweizhi.x += self.zidansudu
            game.blit(self.zidanwaixingr, (self.zidanweizhi.x, self.zidanweizhi.y))

    def zi(self,game):
        game.blit(self.zidanbaozha, (self.zidanweizhi.x, self.zidanweizhi.y))
        pass
#敌机子弹类
class dijizidan(zidan):

    def __init__(self,zidanweizhi,zidanfangxiang):
        self.zidansudu = config.DIJIZIDANSEEPS
        self.zidantiji = config.DIJIZIDANTIJI
        self.zidanat = config.DIJIZIDANWEILI
        self.zidanfangxiang = zidanfangxiang
        self.zidanweizhi = pygame.Rect(zidanweizhi, config.DIJIZIDANTIJI)
        self.zidanwaixingr = pygame.image.load(config.DIJIZIDANWAIGUANR)
        self.zidanwaixingl = pygame.image.load(config.DIJIZIDANWAIGUANL)
        self.zidanwaixingu = pygame.image.load(config.DIJIZIDANWAIGUANU)
        self.zidanwaixingd = pygame.image.load(config.DIJIZIDANWAIGUAND)
        self.zidanbaozha = pygame.image.load(config.DIJIZIDANBAOZHA)

    def feixing(self, game):
        super().zidanfeixing(game)
    def baozha(self,game):
        super().zi(game)
