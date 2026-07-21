class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            goal = 0
            for i in range(l, r + 1):
                goal = max(goal, i + nums[i])
            l = r + 1
            r = goal
            res += 1

        return res 