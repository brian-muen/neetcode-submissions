class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))

        res = 1

        for i in range(len(nums) - 2, -1, -1):
            curr = nums[i]
            
            for j in range(i, len(nums)):
                if curr < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])       

            res = max(res, dp[i])

        return res
