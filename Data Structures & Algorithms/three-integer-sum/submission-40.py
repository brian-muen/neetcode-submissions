class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        length = len(nums) 
        res = []

        for i in range(length - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            lo = i + 1 
            hi = length - 1
            while lo < hi:
                num_hi = nums[hi]
                num_lo = nums[lo]

                if num_hi + num_lo < target:
                    lo += 1 
                elif num_hi + num_lo > target:
                    hi -= 1
                else: 
                    res.append([num_hi, num_lo, nums[i]])
                    lo += 1
                    while nums[lo] == nums[lo - 1] and lo < hi:
                        lo += 1

        return res