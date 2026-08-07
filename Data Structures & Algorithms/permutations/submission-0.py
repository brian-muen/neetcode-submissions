class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        curr = []
        res = []
        pick = [False] * len(nums)
        
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    curr.append(nums[i])
                    pick[i] = True
                    backtrack(curr)
                    curr.pop()
                    pick[i] = False

        backtrack(curr)
        

        return res