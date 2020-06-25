import threading
from catTrace import catTraceT
from catEmulator import catEmulatorT

if __name__ == "__main__":
    catE = CatEmulatorT()
    catT = CatTraceT()
    catE.start()
    catT.start()
    catE.join()
    catT.flag = False
    catT.join()