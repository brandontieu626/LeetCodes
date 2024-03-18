class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #[leetcode] (8)
        dp=[False] * (len(s)+1)
        dp[len(s)]=True
        #[FFFFFFFFT]
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if i+len(word)<=len(s) and s[i:i+len(word)]==word:
                    dp[i]=dp[i+len(word)]
                if dp[i]:
                    break
        
        return dp[0]