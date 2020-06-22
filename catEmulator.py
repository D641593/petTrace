import pygame, time
from pygame.locals import *
import queue
import threading
import math

#使用說明
#使用鍵盤"上下左右"控制貓貓
#另一視窗會顯示貓貓移動路徑
#上下相反是由於兩個視窗的(0,0)不同，貓貓在左上角，路徑在左下角
#關閉請直接關閉貓貓視窗，路徑視窗會自動關閉

anchor_DisQ = queue.Queue()

class catEmulatorT(threading.Thread):
    def __init__(self,name = "catEmulator",flag = True,anchor_x = [400,400,200,200],anchor_y = [400,200,200,400],X = 300,Y = 300):
        threading.Thread.__init__(self)
        self.name = name
        self.flag = flag
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        self.X = X
        self.Y = Y
        self.height = 64*8
        self.width = 64*10

    def run(self):

        pygame.init()
        pygame.font.init()

        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Pygame Cat Emulator')
        pygame.mouse.set_visible(0)

        keyPressed = [False,False,False,False]

        cat = pygame.image.load("cat.jpg")
        marker = pygame.image.load("marker.jpg")

        while self.flag:
            # print("doing a function")
            screen.fill((255,255,255)) # 清空畫面
            for i in range(4):
                screen.blit(marker,(self.anchor_x[i],self.anchor_y[i]))
            screen.blit(cat,(self.X,self.Y)) # 顯示貓
            pygame.display.flip() #更新畫面

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.flag = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        keyPressed[0] = True
                    elif event.key == pygame.K_DOWN:
                        keyPressed[1] = True
                    elif event.key == pygame.K_LEFT:
                        keyPressed[2] = True
                    elif event.key == pygame.K_RIGHT:
                        keyPressed[3] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        keyPressed[0] = False
                    elif event.key == pygame.K_DOWN:
                        keyPressed[1] = False
                    elif event.key == pygame.K_LEFT:
                        keyPressed[2] = False
                    elif event.key == pygame.K_RIGHT:
                        keyPressed[3] = False

            self.move(keyPressed)
            anchor_DisQ.put(self.cal_dis(self.X,self.Y))
            # print(self.cal_dis(self.X,self.Y))
            time.sleep(0.1)

        pygame.quit()

    def move(self,keyPressed:list):
        if len(keyPressed) != 4:
            raise TypeError("Error length of keyPressed",keyPressed)
        for i in keyPressed:
            if type(i) is not bool:
                raise TypeError("keyPressed is not a boolean list",keyPressed)
        if keyPressed[0]:
            if self.Y > 0:
                self.Y -= 15
        elif keyPressed[1]:
            if self.Y < self.height - 64:
                self.Y += 15
        elif keyPressed[2]:
            if self.X > 0:
                self.X -= 15
        elif keyPressed[3]:
            if self.X < self.width - 64:
                self.X += 15

    def get_dis(self,x_off,y_off):
        return round(math.sqrt(math.pow(x_off,2) + math.pow(y_off,2)),2)

    def cal_dis(self,x,y):
        ans = []
        for i in range(4):
            dis = self.get_dis((self.anchor_x[i] - x),(self.anchor_y[i] - y))
            if dis == 0:
                dis += 1
            ans.append(dis)
        return ans
