import datetime as dt
import numpy
#
# following needs to be done.....
# Method for getting Contracts [contract = '<underlying> <date> <month> <strike price> <CE/PE>']
# underlying = given; date  = TBD; month = from list; CE/PE = add as needed while trading;
# strike price = method [need CMP of Underlying, Strike Price Interval, No. of Strikes to generate (default 25)]
# also need method to find CMP of contracts [using kite api]
#

days_of_week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
months_of_year = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
expiry_week_day = 'Thu'

def getActiveMonths():
    activeMonths = []
    tmth = dt.date.today().month -1
    for i in range(3):
        activeMonths.append(months_of_year[tmth + i])
    print(str(activeMonths))
    return activeMonths

def getExpiryDatesforMonth(month, year):
    expiryDates = []
    maxdays = maxdaysinmonth(month)
    if month == 'Feb' and year % 4 == 0:
        maxdays += 1
    for d in range(1, maxdays + 1):
        tdt = dt.date(year, months_of_year.index(month)+1, d)
        if tdt.weekday() == days_of_week.index(expiry_week_day):
            expiryDates.append(d)
    print(str(expiryDates))
    return expiryDates

def getExpiryDatesforCurrentMonth():
    expiryDates = []
    twday = dt.date.today().weekday()
    tdt = dt.date.today().day  # date
    if twday == days_of_week.index(expiry_week_day):
        while tdt < 32:
            expiryDates.append(tdt)
            tdt += 7
    elif twday < days_of_week.index(expiry_week_day):
        correction = days_of_week.index(expiry_week_day) - twday
        tdt += correction
        while tdt < 32:
            expiryDates.append(tdt)
            tdt += 7
    elif twday > days_of_week.index(expiry_week_day):
        correction = (6 - twday) + 4
        tdt += correction
        while tdt < 32:
            expiryDates.append(tdt)
            tdt += 7
    else:
        print('something went wrong...')
    print(str(expiryDates))
    return expiryDates


def getStrikes (undrlyng, cmpUndrlyng, stkPrcIntrvl, noStrikes):
    strikes = []
    if undrlyng == '' or cmpUndrlyng <= 0 or cmpUndrlyng == '' or stkPrcIntrvl <= 0 or stkPrcIntrvl == '':
        strikes = []
        return strikes
    if noStrikes <= 0 or noStrikes == '':
        noStrikes = 25
    # print('No. of Strikes: ', noStrikes)
    if cmpUndrlyng % stkPrcIntrvl == 0:
        strikes.append(cmpUndrlyng)
    else:
        if cmpUndrlyng == int(cmpUndrlyng) and stkPrcIntrvl == int(stkPrcIntrvl):
            for tmpstk in range(cmpUndrlyng, cmpUndrlyng + stkPrcIntrvl):
                if tmpstk % stkPrcIntrvl == 0:
                    strikes.append(tmpstk)
            for tmpstk in range(cmpUndrlyng, cmpUndrlyng - stkPrcIntrvl, -1):
                if tmpstk % stkPrcIntrvl == 0:
                    strikes.append(tmpstk)
        else:
            for tmpstk in numpy.arange(float(cmpUndrlyng), float(cmpUndrlyng) + float(stkPrcIntrvl), float(.05)):
                if float(tmpstk) % float(stkPrcIntrvl) == 0:
                    strikes.append(float(tmpstk))
            for tmpstk in numpy.arange(float(cmpUndrlyng), float(cmpUndrlyng) - float(stkPrcIntrvl), float(-.05)):
                if float(tmpstk) % float(stkPrcIntrvl) == 0:
                    strikes.append(float(tmpstk))
    if len(strikes) == 1:
        tmpstk = strikes[0]
        for i in range(1, noStrikes):
            strikes.append(tmpstk + (i * stkPrcIntrvl))
            strikes.append(tmpstk - (i * stkPrcIntrvl))
    elif len(strikes) == 2:
        tmpstk = strikes[0]
        for i in range(1, noStrikes):
            strikes.append(tmpstk + (i * stkPrcIntrvl))
        tmpstk = strikes[1]
        for i in range(1, noStrikes):
            strikes.append(tmpstk - (i * stkPrcIntrvl))
    else:
        print('something went wrong...')
    strikes.sort()
    print(str(strikes))
    return strikes

def getMonthlyContracts(undrlyng, month, cmpUndrlyng, stkPrcIntrvl, noStrikes):
    contracts = []
    calls = []
    puts = []
    strikes = getStrikes(undrlyng, cmpUndrlyng, stkPrcIntrvl, noStrikes)
    activeMonths = getActiveMonths()
    if month in activeMonths:
        for stk in strikes:
            tcon = undrlyng + ' ' + month + ' ' + str(stk)
            calls.append(tcon + ' CE')
            puts.append(tcon + ' PE')
    else:
        print('Month Invalid...')
    contracts.append(calls)
    contracts.append(puts)
    print(str(calls))
    print(str(puts))
    print(str(contracts))
    return contracts

def getWeeklyContractsforMonth(undrlyng, date, month, year, cmpUndrlyng, stkPrcIntrvl, noStrikes):
    contracts = []
    calls = []
    puts = []
    strikes = getStrikes(undrlyng, cmpUndrlyng, stkPrcIntrvl, noStrikes)
    dates = getExpiryDatesforMonth(month, year)
    activeMonths = getActiveMonths()
    if month in activeMonths and date in dates:
        for stk in strikes:
            tcon = undrlyng + ' ' + str(date) + NumbSuffix(date) + ' ' + month + ' ' + str(stk)
            calls.append(tcon + ' CE')
            puts.append(tcon + ' PE')
    else:
        print('Date / Month Invalid...')
    contracts.append(calls)
    contracts.append(puts)
    print(str(calls))
    print(str(puts))
    print(str(contracts))
    return contracts


def getWeeklyContractsforCurrentMonth(undrlyng, date, month, cmpUndrlyng, stkPrcIntrvl, noStrikes):
    contracts = []
    calls = []
    puts = []
    strikes = getStrikes(undrlyng, cmpUndrlyng, stkPrcIntrvl, noStrikes)
    dates = getExpiryDatesforCurrentMonth()
    activeMonths = getActiveMonths()
    if month in activeMonths and date in dates:
        for stk in strikes:
            tcon = undrlyng + ' ' + str(date) + NumbSuffix(date) + ' ' + month + ' ' + str(stk)
            calls.append(tcon + ' CE')
            puts.append(tcon + ' PE')
    else:
        print('Date / Month Invalid...')
    contracts.append(calls)
    contracts.append(puts)
    print(str(calls))
    print(str(puts))
    print(str(contracts))
    return contracts

def NumbSuffix(numb):
    suffix = {
        1: 'st',
        2: 'nd',
        3: 'rd',
        11: 'th',
        12: 'th',
        13: 'th',
        21: 'st',
        22: 'nd',
        23: 'rd',
        31: 'st'
    }
    return suffix.get(numb, 'th')

def maxdaysinmonth(month):
    daysinmonth = {
        'Jan': 31,
        'Feb': 28,
        'Mar': 31,
        'Apr': 30,
        'May': 31,
        'Jun': 30,
        'Jul': 31,
        'Aug': 31,
        'Sep': 30,
        'Oct': 31,
        'Nov': 30,
        'Dec': 31
    }
    return daysinmonth.get(month)


# getStrikes('lt', 1050, 20, 2)
# getExpiryDatesforCurrentMonth()
# getExpiryDatesforMonth('Jul', 2020)
# getActiveMonths()
# getMonthlyContracts('ONGC', 'May', 79.9, 2.5, 5)
# getWeeklyContractsforCurrentMonth('ONGC', 14, 'May', 79.9, 2.5, 5)
getWeeklyContractsforMonth('ONGC', 16, 'Jul', 2020, 79.9, 2.5, 5)
