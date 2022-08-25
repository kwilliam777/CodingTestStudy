class Solution(object):
    def coinChange(self, coins, amount):
        rs = [amount+1] * (amount+1)
        rs[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    print(i,c,rs)
                    rs[i] = min(rs[i], rs[i-c] + 1)

        return -1 if rs[amount] == amount+1 else rs[amount]
