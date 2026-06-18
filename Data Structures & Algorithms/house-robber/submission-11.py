class Solution:
    def rob(self, nums: List[int]) -> int:
        profit = {}

        profit[0] = nums[0]
        if len(nums) == 1: return profit[0]
        
        profit[1] = max(nums[0], nums[1])
        if len(nums) == 2: return profit[1]        

        for i in range(2, len(nums)):
            profit[i] = max(profit[i - 1], nums[i] + profit[i - 2])


        return profit[len(nums) - 1]