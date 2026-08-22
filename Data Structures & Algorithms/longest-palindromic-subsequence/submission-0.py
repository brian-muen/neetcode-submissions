class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
    
        dp = [[0] * len(s) for i in range(len(s))]

        for right in range(len(s)):
            dp[right][right] = 1
            for left in range(right - 1, -1, -1):
                if s[left] == s[right]:
                    dp[left][right] = 2 + dp[left + 1][right - 1]
                else:
                    dp[left][right] = max(dp[left + 1][right], dp[left][right -1])

        return dp[0][len(s) - 1]