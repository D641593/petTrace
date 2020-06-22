from PointCalculation import pointCalculation
import turtle as tl
import threading
from catEmulator import anchor_DisQ
import pygame

class catTraceT(threading.Thread):
    def __init__(self,name = "catTrace",flag = True,anchor_x = [400,400,200,200],anchor_y = [400,200,200,400]):
        threading.Thread.__init__(self)
        self.name = name
        self.flag = flag
        self.anchor_x = anchor_x
        self.anchor_y = anchor_y
        self.pc = pointCalculation(self.anchor_x,self.anchor_y)
        self.anchorsGroup = self.pc.get_group(len(self.anchor_x))
        self.colors = ["blue","black","green","purple"]

    def run(self):
        # ---------------------------   DrawInit       -------------------------
        tl.screensize(64 * 20, 64 * 16)
        tl.speed(20)
        tl.penup()
        canvas = tl.getcanvas()
        canvas.config(xscrollincrement = str(100))
        canvas.config(yscrollincrement = str(100))
        canvas.yview_scroll(2,'unit')
        canvas.xview_scroll(3,'unit')
        for i in range(len(self.anchor_x)):
            tl.color(self.colors[i])
            tl.goto(self.anchor_x[i],-1 * self.anchor_y[i])
            tl.stamp()
        tl.color("red")
        # ---------------------------   DrawInit       -------------------------

        # ---------------------------   LocateByCode   -------------------------       
        while True:
            while anchor_DisQ.qsize() == 0 and self.flag:
                pass
            if not self.flag:
                break
            tl.color("grey")
            tl.stamp()

            
            distances = anchor_DisQ.get()
            self.pc.set_dis(distances)
            points = self.pc.get_cal_array(self.anchorsGroup)
            if points is None:
                continue
            try:
                finalPoint = self.pc.get_close_point(points)
            except ValueError as e:
                print(repr(e))
                continue
            tl.color("red")
            tl.goto(finalPoint[0],-1 * finalPoint[1])
            tl.stamp()
        
        # ---------------------------   LocateByCode   ------------------------- 
