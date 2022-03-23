import csvReader
import StopLoss
import tick


def changeOrderPosition(sl):
    if sl.positiontype.lower() == 'buy':
        sl.positiontype = 'sell'
    else:
        sl.positiontype = 'buy'

def main():
    # Main logic / workflow for bot
    # ----------------------- init section ----------------------------
    stks = csvReader.readcsv('./data/LT-EQ.csv')
    sl = StopLoss.StopLoss
    stks.reverse()
    sl.positiontype = 'sell'  # change to buy / sell - depending on requirements
    sl.currentprice = float(stks[0][1])
    sl.sltppercent = float(0.3)
    sl.sltp = float(sl.GetSLTP(sl.positiontype, sl.currentprice, sl.sltppercent))
    sl.prevdynsltp = sl.sltp
    sl.dynamicsltp = sl.sltp
    sl.sltptriggeredcheck = False
    sl.dynsltptriggeredcheck = True
    entryprice = sl.currentprice
    exitprice = 0
    totalpnl = []
    # ----------------------- init section ----------------------------

    print("\nPrinting open ticks and dyn sltp data...")
    print("Stock: L&T Eq | SLTP%: ", sl.sltppercent, " timestamp: ", stks[0][0])
    print("")
    print("Cur Price  |  SLTP  |  Dyn SLTP  |  Comments ")
    opens = []
    for i in stks:
        # print(float(i[1]))
        opens.append(float(i[1]))

    for op in opens:
        sl.currentprice = op
        sl.dynamicsltp = float(sl.GetDynamicSLTP(sl.positiontype, sl.currentprice, sl.sltppercent, sl.prevdynsltp))
        if not sl.IsDynamicSLTPTriggered(sl.positiontype, sl.currentprice, sl.dynamicsltp):
            # dyn sltp not triggered
            if opens[0] == op or opens[-1] == op:
                if op == opens[0]:
                    entryprice = sl.currentprice
                    print(round(sl.currentprice, 2), ' | ', round(sl.sltp, 2), ' | ', round(sl.dynamicsltp, 2), ' | ',
                          'Placed \'' + str(sl.positiontype) + '\' Position order (Market Opening)...')
                sl.sltp = float(sl.GetSLTP(sl.positiontype, sl.currentprice, sl.sltppercent))
                sl.prevdynsltp = float(sl.sltp)
                sl.dynamicsltp = float(
                    sl.GetDynamicSLTP(sl.positiontype, sl.currentprice, sl.sltppercent, sl.prevdynsltp))
                if op == opens[-1]:
                    changeOrderPosition(sl)
                    print(round(sl.currentprice, 2), ' | ', round(sl.sltp, 2), ' | ', round(sl.dynamicsltp, 2), ' | ',
                          'Placed \'' + str(sl.positiontype) + '\' Position order (Market Closing)...')
                    changeOrderPosition(sl)
                    exitprice = sl.currentprice
                    profitorloss = exitprice - entryprice
                    if sl.positiontype == 'sell':
                        profitorloss *= -1
                    totalpnl.append(profitorloss)
                    print('Entry Price: ', round(float(entryprice), 2), ' | ', 'Exit Price: ',
                          round(float(exitprice), 2), ' | ', 'Position Type: \'' + str(sl.positiontype) + '\' ', ' | ',
                          'Profit / Loss: ', round(float(profitorloss), 2), ' | ')
                    print('Total Profit / Loss for the day : Rs. ', round(float(sum(totalpnl)), 2))
            else:
                print(round(sl.currentprice, 2), ' | ', round(sl.sltp, 2), ' | ', round(sl.dynamicsltp, 2), ' | ')
        else:
            # dyn sltp triggered
            sl.dynsltptriggeredcheck = True
            print(round(sl.currentprice, 2), ' | ', round(sl.sltp, 2), ' | ', round(sl.dynamicsltp, 2), ' | ',
                  'dyn sltp triggered -> Position reversed...')
            exitprice = sl.currentprice
            profitorloss = exitprice - entryprice
            if sl.positiontype == 'sell':
                profitorloss *= -1
            print('Entry Price: ', round(float(entryprice), 2), ' | ', 'Exit Price: ', round(float(exitprice), 2), ' | ', 'Position Type: \'' + str(sl.positiontype) + '\' ', ' | ', 'Profit / Loss: ', round(float(profitorloss), 2), ' | ')
            totalpnl.append(profitorloss)
            if profitorloss <= 0:
                changeOrderPosition(sl)
            if sl.dynsltptriggeredcheck == True:
                sl.sltp = float(sl.GetSLTP(sl.positiontype, sl.currentprice, sl.sltppercent))
                sl.prevdynsltp = float(sl.sltp)
                sl.dynamicsltp = float(
                    sl.GetDynamicSLTP(sl.positiontype, sl.currentprice, sl.sltppercent, sl.prevdynsltp))
                print(round(sl.currentprice, 2), ' | ', round(sl.sltp, 2), ' | ', round(sl.dynamicsltp, 2), ' | ',
                      'Placed \'' + str(sl.positiontype) + '\' Position order...')
                entryprice = sl.currentprice
                sl.dynsltptriggeredcheck = False
        sl.prevdynsltp = float(sl.dynamicsltp)

main()
