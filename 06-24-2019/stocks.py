#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


def maxProfit(prices = []) -> int:

        if len(prices) <= 1:
            return 0

        minValue = prices[0]
        result = 0

        for i in range(1, len(prices)):
            if prices[i] < minValue:
                minValue = prices[i]
            profit = prices[i] - minValue
            if profit > result:
                result = profit

        return result


print("The profit for [3,2,7,1,4,6] is: "+str(maxProfit([3,2,7,1,4,6]))+".")
print("The profit for [] is: "+str(maxProfit([]))+".")
print("The profit for [3] is: "+str(maxProfit([3]))+".")
print("The profit for [3,2,7,1,4,6,10] is: "+str(maxProfit([3,2,7,1,10,4,6]))+".")
