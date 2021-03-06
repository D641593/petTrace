import unittest
from catTrace import CatTraceT
from catEmulator import CatEmulatorT,anchor_disq
import time

class CatTraceTest(unittest.TestCase):
    catT = CatTraceT()
    catE = CatEmulatorT()

    def test_run(self):
        self.catE.start()
        self.catT.start()
        anchor_disq.put([50,50,50,50])
        anchor_disq.put([141,123,208,156])
        time.sleep(2)
        self.catE.flag = False
        self.catE.join()
        self.catT.flag = False
        self.catT.join()

# unittest.main()