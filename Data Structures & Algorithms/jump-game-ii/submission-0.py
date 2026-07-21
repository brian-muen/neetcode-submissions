class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        goal = n - 1
        res = 0

        while goal != 0:
            champ = float('inf')
            for i in range(goal - 1, -1, -1):
                if nums[i] + i >= goal:
                    champ = min(i, champ)
            goal = champ
            res += 1
        
        return res
            
        





        