import math

class emadiff:
    def twe_hund_ema_diff(twema, hundema):
        return abs(twema - hundema)

    def wrapper_Least_ema_diff(stocks, twemas, hundemas):
        Stocks_short_list = []
        # least_emadiff = 100
        threshold = 0.25
        for stock, tema, hundema in range(stocks, twemas, hundemas):
            tempdiff = twe_hund_ema_diff(twema, hundema)
            if tempdiff <= threshold:
                Stocks_short_list.append(stock)
        return Stocks_short_list
