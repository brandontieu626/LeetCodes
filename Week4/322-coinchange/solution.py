class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for v in range(amount+1):
            for c in coins:
                if v>=c:
                    dp[v]=min(dp[v],dp[v-c]+1)
        
        if dp[amount]==amount+1:
            return -1
        
        return dp[amount]
        
        