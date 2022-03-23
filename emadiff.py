import math

class emadiff:
    def twe_hund_ema_diff(twema, hundema):
        return abs(twema - hundema)

    def wrapper_Least_ema_diff(stocks, twemas, hundemas):
        Stocks_short_list = []
        threshold = 0.25
        stock_list_size = len(stocks)
        if stock_list_size == len(twemas) and stock_list_size == len(hundemas):
            for i in range(stock_list_size):
                tempdiff = twe_hund_ema_diff(twemas[i], hundemas[i])
                if tempdiff <= threshold:
                    Stocks_short_list.append(stocks[i])
        else:
            print('List length mismatch - ensure that all 3 lists are of the same size...')
        return Stocks_short_list
