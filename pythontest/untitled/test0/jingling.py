import pygame

class magifeiji(pygame.sprite.Sprite):

    def __init__(self,feijitupian,speed):

        super().__init__()

        self.image=pygame.image.load("./res/dijibaozha.gif")
        self.rect=self.image.get_rect()
        self.speed=speed


    def update(self, ):

        pygame.sprite.Group()

        pass
    pygame.init()
    pygame.display.set_mode((200,200))
while True:


    for event in pygame.event.get():
        #pygame.key.get_pressed()

        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            print(event.type)

    k=pygame.key.get_pressed()
    if k[pygame.K_RIGHT]:
        print("r")



    clock=pygame.time.Clock()
    clock.tick(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()