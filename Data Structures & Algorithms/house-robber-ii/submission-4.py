class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        profit = {}

        if length == 1: return nums[0]
        profit[0] = nums[0]
        if length == 2: return max(nums[0], nums[1])
        profit[1] = max(nums[0], nums[1])


        for i in range(2, length - 1):
            profit[i] = max(nums[i] + profit[i - 2], profit[i - 1])
        res = profit[length - 2]

        profit2 = {}
        profit2[1] = nums[1]
        profit2[2] = max(nums[1], nums[2])
        for i in range(3, length):
            profit2[i] = max(nums[i] + profit2[i - 2], profit2[i - 1])




        return max(profit[length - 2], profit2[length - 1])
            
        