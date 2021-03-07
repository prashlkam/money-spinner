import datetime as dt
import random as r
import candlestick

def ticks(dur, rv1, rv2):
    # to get random ticks between a range for every second
    # dur = number of seconds for which ticks are needed
    i = 0
    tcks = []
    while i < dur:
        tmp = []
        t = []
        for j in range(3):
        # to get upper and lower limit of subrange
        # why 3? -> on some occasions 2 successive random values turn out to be the same (but never 3)
            if rv1 == int(rv1) and rv2 == int(rv2):
                rval1 = r.randrange(rv1, rv2)
            else:
                rval1 = round(r.uniform(rv1, rv2), 2)
            tmp.append(rval1)
        print(str(tmp))
        r1 = min(tmp)
        r2 = max(tmp)
        print(r1, r2)
        sec1 = dt.datetime.now().second
        sec2 = sec1
        cnt = 1
        while sec1 == sec2:
        # get random ticks within subrange for each second
            if r1 == int(r1) and r2 == int(r2):
                rval2 = r.randrange(r1, r2)
            else:
                rval2 = round(r.uniform(r1, r2), 2)
            t.append(rval2)
            sec2 = dt.datetime.now().second
            cnt += 1
        i += 1
        tcks.append(t)
    return tcks

def makecandles (tcks, base):
    # tcks -> continous stream of ticks (some 20k per sec)
    # base -> candlestick data for that minute - one set of OHLC data
    # this function aims to make candkesticks for every second in the 'base' minute......
    csticks = []
    for t in tcks:
        cs = candlestick.candlestick
        cs.tstmp = base.tstmp
        cs.opn = t[0]
        cs.hgh = max(t)
        cs.low = min(t)
        cs.clo = t[-1]
        cs.vol = base.vol
        csticks.append(cs)
    return csticks

# ticks3secs = ticks(3, 1950, 2500)
# f = open("./data/ticksfile1.txt", "w")
# f.write(str(ticks3secs))
# f.close()
