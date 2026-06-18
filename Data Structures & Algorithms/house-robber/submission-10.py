class Solution:
    def rob(self, nums: List[int]) -> int:

        profit = {}

        profit[0] = nums[0]

        if len(nums) == 1: return nums[0]

        if nums[1] > nums[0]:
            profit[1] = nums[1]
        else:
            profit[1] = nums[0]

        if len(nums) == 2: return profit[1]

        for i in range(2, len(nums)):
            profit[i] = nums[i] + profit[i - 2]
            if profit[i] < profit[i - 1]:
                profit[i] = profit[i - 1]


        return profit[len(nums) - 1]