

class candlestick:
    def __init__(self, tstmp, opn, hgh, low, clo, vol):
        self.tstmp = str(tstmp)
        self.opn = float(opn)
        self.hgh = float(hgh)
        self.low = float(low)
        self.clo = float(clo)
        self.vol = int(vol)
