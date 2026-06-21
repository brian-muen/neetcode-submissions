class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 1

        if len(seen) == 0:
            return 0

        for num in nums:
            count = 1
            if (num - 1) in seen:
                continue
            while num + count in seen:
                count += 1
                longest = max(longest, count)
        
        return longest

        

        