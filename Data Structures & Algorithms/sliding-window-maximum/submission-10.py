class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        for i in range(k):
            window.append((-1 * nums[i], i))

        heapq.heapify(window)

        res = [-1 * window[0][0]]

        l = 0
        r = k

        while r < len(nums):
            new = -1 * nums[r]
            heapq.heappush(window, (new, r))
            
            while window[0][1] <= l:
                heapq.heappop(window)

            res.append(-1 * window[0][0])

            l += 1
            r += 1

        return res
        