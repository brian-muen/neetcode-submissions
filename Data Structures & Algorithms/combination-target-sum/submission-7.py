class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        path = []

        def backtrack(start, target):
            if target == 0:
                res.append(path.copy())
            for i in range(start, len(nums)):
                if nums[i] > target:
                    break
                
                path.append(nums[i])
                backtrack(i, target - nums[i])

                path.pop()


        backtrack(0, target)

        return res









            