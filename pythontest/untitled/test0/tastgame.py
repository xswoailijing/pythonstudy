import pygame
import time

chuanglouweizhi=(500,500)
pygame.init()



re=pygame.Rect(10,10,50,50)
game=pygame.display.set_mode(chuanglouweizhi)

b=pygame.image.load("./testproject/场景2.jpg")

game.blit(b,(0,0))
pygame.display.update()


while True:
    time.sleep(1)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



pygame.quit()






def main():

    pass








if __name__ == '__main__':
    main()
