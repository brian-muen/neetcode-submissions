import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = [-x for x in nums[:k]]
        heapq.heapify(window)

        res = [-window[0]]

        l = 0
        r = k

        while r < len(nums):
            old = -1 * nums[l]
            window.remove(old)
            heapq.heapify(window)

            new = -1 * nums[r]
            heapq.heappush(window, new)
            
            res.append(-window[0])

            l += 1
            r += 1

        return res