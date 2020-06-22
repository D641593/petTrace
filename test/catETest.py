from catEmulator import *
import unittest

class catEmulatorTest(unittest.TestCase):
    catE = catEmulatorT() 
    def test_get_dis(self):
        res = self.catE.get_dis(3,4)
        self.assertEqual(res,5)

    def test_cal_dis(self):
        res = self.catE.cal_dis(300,300)
        ans = [141.42]*4
        self.assertEqual(res,ans)

    def test_move1(self):
        keyPressed = [True,False,False,False]
        self.catE.Y = 300
        self.catE.move(keyPressed)
        self.assertEqual(self.catE.Y,285)

    def test_move1_Block(self):
        keyPressed = [True,False,False,False]
        self.catE.Y = 0
        self.catE.move(keyPressed)
        self.assertEqual(self.catE.Y,0)

    def test_move2(self):
        keyPressed = [False,True,False,False]
        self.catE.Y = 300
        self.catE.move(keyPressed)
        self.assertEqual(self.catE.Y,315)

    def test_move2_Block(self):
        keyPressed = [False,True,False,False]
        self.catE.Y = self.catE.height
        self.catE.move(keyPressed)
        self.assertEqual(self.catE.Y,self.catE.height)

    def test_move3(self):
        keyPressed = [False,False,True,False]
        self.catE.X = 300
        self.catE.move(keyPressed)
        self.assertEqual(self.catE.X,285)

    def test_move3_Block(self):
        keyPressed = [False,False,True,False]
        self.catE.X = 0
        self.catE.move(keyPressed)
        self.assertEqual(self.catE.X,0)

    def test_move4(self):
        keyPressed = [False,False,False,True]
        self.catE.X = 300
        self.catE.move(keyPressed)
        self.assertEqual(self.catE.X,315)

    def test_move4_Block(self):
        keyPressed = [False,False,False,True]
        self.catE.X = self.catE.width
        self.catE.move(keyPressed)
        self.assertEqual(self.catE.X,self.catE.width)

    def test_move_TypeError1(self):
        with self.assertRaises(TypeError):
            keyPressed = [False,False,False]
            self.catE.move(keyPressed)

    def test_move_TypeError2(self):
        with self.assertRaises(TypeError):
            keyPressed = [False,True,False,4]
            self.catE.move(keyPressed)
    
    def test_move_TypeError3(self):
        with self.assertRaises(TypeError):
            keyPressed = [3,False,True,False]
            self.catE.move(keyPressed)

    def test_run(self):
        self.catE.X = 300
        self.catE.Y = 300
        self.catE.start()
        time.sleep(1)
        self.catE.flag = False
        self.catE.join()
        

# unittest.main()

