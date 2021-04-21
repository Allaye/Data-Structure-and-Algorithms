# Task! you have a daily price of gold for an interval of time, you want to find two days internet
# in this interval such that if you have bought then sold gold at those dates you'd have made the
# maximum possible profit. You

# use the Kadane Algorithm

def trade(prices):
    sell_day = 1
    buy_day = 1
    best_profit = 0
    for s in range(2, len(prices)):
        if prices[s] < prices[buy_day]:
            b = s
        else:
            b = buy_day
        profit = prices[s] - prices[b]
        if profit < best_profit:
            sell_day = s
            buy_day = b
            best_profit = profit
    return sell_day, buy_day


prices = [1, 1, 2, 3, 4, 5, 6]
print(prices)
print(trade(prices))
