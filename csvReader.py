import csv

def readcsv (filename):
    reader = csv.reader(open(filename, 'r'))
    i = 0
    cstks = []
    #cs = candlestick.candlestick
    for row in reader:
        if i == 0:
            i += 1
            continue
        else:
            # print(row)
            # cs.tstmp = str(row[0])
            # cs.opn = float(row[1])
            # cs.hgh = float(row[2])
            # cs.low = float(row[3])
            # cs.clo = float(row[4])
            # cs.vol = int(row[5])
            cstks.append(row)
            i += 1
        # cs = candlestick.candlestick
    # print(cstks)
    return cstks
