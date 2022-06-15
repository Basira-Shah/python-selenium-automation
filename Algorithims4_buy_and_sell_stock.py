# O(n)
def buy_and_sell_stock(prices):
    max_sum = cur_sum = 0
    for i in range(len(prices) -1):
        cur_sum = cur_sum + prices[i + 1] - prices[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
        if cur_sum < 0:
            cur_sum = 0

    return max_sum


test_prices = [7, 1, 5, 3, 6,  4]  # resturn 5
print(buy_and_sell_stock(test_prices))