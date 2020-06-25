import unittest
from catTrace import *
from catEmulator import *
import time

class catTraceTest(unittest.TestCase):
    catT = CatTraceT()
    catE = CatEmulatorT()

    def test_run(self):
        self.catE.start()
        self.catT.start()
        anchor_DisQ.put([50,50,50,50])
        anchor_DisQ.put([141,123,208,156])
        time.sleep(2)
        self.catE.flag = False
        self.catE.join()
        self.catT.flag = False
        self.catT.join()

# unittest.main()