import pygame, time
import queue
import threading
import math
import time

#使用說明
#使用鍵盤"上下左右"控制貓貓
#另一視窗會顯示貓貓移動路徑
#上下相反是由於兩個視窗的(0,0)不同，貓貓在左上角，路徑在左下角
#關閉請直接關閉貓貓視窗，路徑視窗會自動關閉

anchor_disq = queue.Queue()

class CatEmulatorT(threading.Thread):
    def __init__(self,name = "catEmulator",flag = True,x = 300,y = 300):
        threading.Thread.__init__(self)
        self.name = name
        self.flag = flag
        self.anchor_x = [400,400,200,200]
        self.anchor_y = [400,200,200,400]
        self.x = x
        self.y = y
        self.height = 64*8
        self.width = 64*10

    def run(self):

        pygame.init()
        pygame.font.init()

        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Pygame Cat Emulator')
        pygame.mouse.set_visible(0)

        keypressed = [False,False,False,False]

        cat = pygame.image.load("cat.jpg")
        marker = pygame.image.load("marker.jpg")

        while self.flag:
            # print("doing a function")
            screen.fill((255,255,255)) # 清空畫面
            for i in range(4):
                screen.blit(marker,(self.anchor_x[i],self.anchor_y[i]))
            screen.blit(cat,(self.x,self.y)) # 顯示貓
            pygame.display.flip() #更新畫面

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.flag = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        keypressed[0] = True
                    elif event.key == pygame.K_DOWN:
                        keypressed[1] = True
                    elif event.key == pygame.K_LEFT:
                        keypressed[2] = True
                    elif event.key == pygame.K_RIGHT:
                        keypressed[3] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        keypressed[0] = False
                    elif event.key == pygame.K_DOWN:
                        keypressed[1] = False
                    elif event.key == pygame.K_LEFT:
                        keypressed[2] = False
                    elif event.key == pygame.K_RIGHT:
                        keypressed[3] = False

            self.move(keypressed)
            anchor_disq.put(self.cal_dis(self.x,self.y))
            time.sleep(0.1)

        pygame.quit()

    def move(self,keypressed:list):
        if len(keypressed) != 4:
            raise TypeError("Error length of keypressed",keypressed)
        for i in keypressed:
            if type(i) is not bool:
                raise TypeError("keypressed is not a boolean list",keypressed)
        if keypressed[0]:
            if self.y > 0:
                self.y -= 15
        elif keypressed[1]:
            if self.y < self.height - 64:
                self.y += 15
        elif keypressed[2]:
            if self.x > 0:
                self.x -= 15
        elif keypressed[3]:
            if self.x < self.width - 64:
                self.x += 15

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
