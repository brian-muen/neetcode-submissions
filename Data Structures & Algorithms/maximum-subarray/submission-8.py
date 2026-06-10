class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
         
        running_sum = 0
        res = -1000000000000

        for i in range(n):
            running_sum += nums[i]
            res = max(running_sum, res)
            if running_sum < 0:
                running_sum = 0
        
        return res
