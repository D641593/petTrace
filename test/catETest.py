from catEmulator import CatEmulatorT
import unittest
import time

class CatEmulatorTest(unittest.TestCase):
    catE = CatEmulatorT() 
    def test_get_dis(self):
        res = self.catE.get_dis(3,4)
        self.assertEqual(res,5)

    def test_cal_dis(self):
        res = self.catE.cal_dis(300,300)
        ans = [141.42]*4
        self.assertEqual(res,ans)

    def test_move1(self):
        keypressed = [True,False,False,False]
        self.catE.y = 300
        self.catE.move(keypressed)
        self.assertEqual(self.catE.y,285)

    def test_move1_Block(self):
        keypressed = [True,False,False,False]
        self.catE.y = 0
        self.catE.move(keypressed)
        self.assertEqual(self.catE.y,0)

    def test_move2(self):
        keypressed = [False,True,False,False]
        self.catE.y = 300
        self.catE.move(keypressed)
        self.assertEqual(self.catE.y,315)

    def test_move2_Block(self):
        keypressed = [False,True,False,False]
        self.catE.y = self.catE.height
        self.catE.move(keypressed)
        self.assertEqual(self.catE.y,self.catE.height)

    def test_move3(self):
        keypressed = [False,False,True,False]
        self.catE.x = 300
        self.catE.move(keypressed)
        self.assertEqual(self.catE.x,285)

    def test_move3_Block(self):
        keypressed = [False,False,True,False]
        self.catE.x = 0
        self.catE.move(keypressed)
        self.assertEqual(self.catE.x,0)

    def test_move4(self):
        keypressed = [False,False,False,True]
        self.catE.x = 300
        self.catE.move(keypressed)
        self.assertEqual(self.catE.x,315)

    def test_move4_Block(self):
        keypressed = [False,False,False,True]
        self.catE.x = self.catE.width
        self.catE.move(keypressed)
        self.assertEqual(self.catE.x,self.catE.width)

    def test_move_TypeError1(self):
        with self.assertRaises(TypeError):
            keypressed = [False,False,False]
            self.catE.move(keypressed)

    def test_move_TypeError2(self):
        with self.assertRaises(TypeError):
            keypressed = [False,True,False,4]
            self.catE.move(keypressed)
    
    def test_move_TypeError3(self):
        with self.assertRaises(TypeError):
            keypressed = [3,False,True,False]
            self.catE.move(keypressed)

    def test_run(self):
        self.catE.x = 300
        self.catE.y = 300
        self.catE.start()
        time.sleep(1)
        self.catE.flag = False
        self.catE.join()

# unittest.main()

