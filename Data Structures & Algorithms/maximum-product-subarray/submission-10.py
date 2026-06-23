class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        curMax = curMin = 1
        
        for num in nums:
            if num == 0:
                curMax = curMin = 1
                res = max(res, 0)
                continue
            
            temp = curMax * num
            curMax = max(num, temp, curMin * num)
            curMin = min(num, temp, curMin * num)

            res = max(res, curMax)



        return res