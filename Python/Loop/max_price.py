stock_prices = [241, 251, 232, 254, 248]


def findMaxPrice(stocks):
    """ find the maximum price among the stock prices """
    # code here
    max_price = 0
    for i in stocks:
        if i > max_price:
            max_price = i
    return max_price


print(findMaxPrice(stock_prices))
