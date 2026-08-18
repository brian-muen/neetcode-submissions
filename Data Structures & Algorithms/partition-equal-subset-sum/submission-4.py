class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False
        else:
            target = sum(nums) // 2
        
        sums = set()
        sums.add(0)
        
        for i in nums:
            sums_copy = set()
            for val in sums:
                if val + i == target:
                    return True
                sums_copy.add(val + i)
                sums_copy.add(val)
            sums = sums_copy
        return False






        
            