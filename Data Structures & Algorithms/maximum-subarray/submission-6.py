class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        running_sum = nums[0]
        min_prefix = min(0, nums[0])
        for i in range(1, len(nums)):
            running_sum += nums[i]
            if running_sum - min_prefix > res:
                res = running_sum - min_prefix
            if running_sum < min_prefix:
                min_prefix = running_sum
        return res
            
        