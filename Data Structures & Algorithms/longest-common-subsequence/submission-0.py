class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        dp = [[0] * (cols + 1) for _ in range(rows + 1)] # dp[i][j] represents LCS of the first i chars of text1 and j chars of text2
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if text1[i - 1] == text2[j - 1]: # last characters match
                    dp[i][j] = 1 + dp[i - 1][j - 1] # include the last character plus the LCS of that character not included
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # at least one of the characters NOT included in LCS: throw away one from str1 and include everything in str2 and vice versa
        return dp[-1][-1]

