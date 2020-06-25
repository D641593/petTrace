import math
import numpy as np
import turtle as tl

class PointCalculation():
    def __init__(self,anchors_x = None,anchors_y = None,anchors_dis = None):
        self.anchors_x = anchors_x
        self.anchors_y = anchors_y
        self.anchors_dis = anchors_dis
    
    def set_dis(self,anchors_dis):
        self.anchors_dis = anchors_dis

    def set_xandy(self,anchors_x,anchors_y):
        self.anchors_x = anchors_x
        self.anchors_y = anchors_y

    def get_cos(self,a,b,c):
        tmp = math.pow(a,2) + math.pow(b,2) - math.pow(c,2)
        div = 2 * a * b
        return round(tmp / div , 2) # cos(c)

    def get_dis(self,a,b,c):
        return round(a * self.get_cos(a,b,c),2)

    def get_anchor_dis(self,x_off,y_off):
        return round(math.sqrt(math.pow(x_off,2) + math.pow(y_off,2)),2)

    def get_group(self,anchor_numbers):
        ans = []
        tmp = []
        if anchor_numbers < 3:
            raise ValueError
        for i in range(anchor_numbers):
            for j in range(i+1,anchor_numbers):
                for n in range(j+1,anchor_numbers):
                    tmp.append(i)
                    tmp.append(j)
                    tmp.append(n)
                    ans.append(tmp.copy())
                    tmp.clear()
        return ans
    
    def check_tri(self,a,b,c):
        if a + b >= c and b + c >= a and a + c >= b:
            return True
        return False
    
    def fit_triangle(self,a,b,c):
        outofrange = 30
        errormessage = "offset is large,Bad Point"
        if a + b < c:
            off = c - a - b
            if off > outofrange:
                raise ValueError(errormessage,a,b,c)
            c -= off / 2
            b += off / 2
        elif b + c < a:
            off = a - b - c
            if off > outofrange:
                raise ValueError(errormessage,a,b,c)
            b += off / 2
            c += off / 2
        elif a + c < b:
            off = b - a - c
            if off > outofrange:
                raise ValueError(errormessage,a,b,c)
            b -= off / 2
            c += off / 2
        return [a,b,c]

    def get_cal_array(self,anchor_groups):
        constlist = []
        paraarray = []
        paratmp = []
        anspoint = []
        for group in anchor_groups:
            start_anchor = group[0]
            for i in group[1:]:
                end_anchor = i
                x_off = self.anchors_x[start_anchor] - self.anchors_x[end_anchor]
                y_off = self.anchors_y[start_anchor] - self.anchors_y[end_anchor]
                dis_between_start_end = self.get_anchor_dis(x_off,y_off)
                dis_start = self.anchors_dis[start_anchor]
                dis_end = self.anchors_dis[end_anchor]
                if not self.check_tri(dis_between_start_end,dis_start,dis_end):
                    try:
                        newdis = self.fit_triangle(dis_between_start_end,dis_start,dis_end)
                        dis_start = newdis[1]
                        dis_end = newdis[2]
                    except ValueError as e:
                        print(repr(e))
                        return None
                cur_off = self.get_dis(dis_start,dis_between_start_end,dis_end)
                proportion = round(cur_off / dis_between_start_end , 2)
                cur_off_x = x_off * proportion
                cur_off_y = y_off * proportion
                point_x = self.anchors_x[start_anchor] - cur_off_x
                point_y = self.anchors_y[start_anchor] - cur_off_y
                if x_off == 0:
                    const = point_y
                    y_off = 1
                elif y_off == 0:
                    const = point_x
                    x_off = 1
                else:
                    const = point_x * x_off + point_y * y_off
                paratmp.append(x_off)
                paratmp.append(y_off)
                paraarray.append(paratmp.copy())
                constlist.append(const)
                paratmp.clear()
            A = np.mat(paraarray)
            paraarray.clear()
            b = np.mat(constlist).T
            constlist.clear()
            r = np.linalg.solve(A,b)
            anspoint.append([r[0,0],r[1,0]])
        return anspoint
    
    def get_point(self,points):
        sum_x = 0
        sum_y = 0
        for i in points:
            sum_x += i[0]
            sum_y += i[1]
        return [ sum_x / len(points) , sum_y / len(points)]

    def get_close_point(self,points): # undone , I need to think
        mark = [0] * len(points)
        offset = 30
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            for j in range(len(points)):
                if i == j:
                    mark[i] += 1
                    continue
                test_x = points[j][0]
                test_y = points[j][1]
                if x + offset > test_x and test_x > x - offset and y + offset > test_y and test_y > y - offset:
                    mark[i] += 1

        max_index = 0
        biggest = 0
        for i in range(len(mark)):
            if mark[i] > biggest:
                biggest = mark[i]
                max_index = i
        if mark[max_index] == 1:
            raise ValueError("Bad Points",points)
        sameflag = 1
        value = mark[0]
        for i in range(len(mark)):
            if mark[i] != value:
                sameflag = 0
        if sameflag:
            sum_x = 0
            sum_y = 0
            for i in range(len(points)):
                sum_x += points[i][0]
                sum_y += points[i][1]
            return [ sum_x / len(points) , sum_y / len(points) ]

        x = points[max_index][0]
        y = points[max_index][1]
        sum_x = 0
        sum_y = 0
        for j in range(len(points)):
            test_x = points[j][0]
            test_y = points[j][1]
            if x + offset > test_x and test_x > x - offset and y + offset > test_y and test_y > y - offset:
                sum_x += points[j][0]
                sum_y += points[j][1]
        return [sum_x / mark[max_index]  , sum_y / mark[max_index]]
                        
                        


        