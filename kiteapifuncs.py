# connect to zerodha kite api
kite = KiteConnect(api_key="your_api_key")

# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
request_token = ""

# Once you have the request_token, obtain the access_token
# as follows.
data = kite.generate_session(request_token, api_secret="your_api_secret")
kite.set_access_token(data["access_token"])

# Place an order
kite.order_place(
    variety=kite.VARIETY_REGULAR,
    exchange=kite.EXCHANGE_NSE,
    tradingsymbol="INFY",
    transaction_type=kite.TRANSACTION_TYPE_BUY,
    quantity=1,
    order_type=kite.ORDER_TYPE_MARKET,
    product=kite.PRODUCT_MIS
)

# get price of stock from zerodha kite api
def get_stock_price(stock_id):
    data = kite.ltp(stock_id)
    return data[0]['last_price']

# get stock data from zerodha kite api
def get_stock_data(stock_id):
    data = kite.quote(stock_id)
    return data[0]

# get a list of stocks in a list
def get_stocks_list(list_id):
    data = kite.ltp(list_id)
    return data

# get a list of stocks in a list
def get_stocks_data(list_id):
    data = kite.quote(list_id)
    return data

# get stock_id from stock name
def get_stock_id(stock_name):
    data = kite.instruments(stock_name)
    return data[0]['instrument_token']


# get list of stocks in a list
def get_list_stocks(list_id):
    data = kite.ltp(list_id)
    return data


