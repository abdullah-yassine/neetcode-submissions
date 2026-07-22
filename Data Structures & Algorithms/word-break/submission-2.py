class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1) # dp[i] : can s[]
        dp[0] = True
        for i in range(len(s) + 1):
            if dp[i]:
                for word in wordDict:
                    if s[i : i + len(word)] == word:
                        dp[i + len(word)] = True
                
        return dp[len(s)]