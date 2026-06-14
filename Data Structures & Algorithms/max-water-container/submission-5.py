class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        left_h = heights[l]
        right_h = heights[r]

        res = min(left_h, right_h) * (r - l)

        while l < r:
            if left_h > right_h:
                r -= 1
                right_h = heights[r]
                res = max(min(left_h, right_h) * (r - l), res)
            else:
                l += 1
                left_h = heights[l]
                res = max(min(left_h, right_h) * (r - l), res)


        return res