class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = [0]

        for idx in range(1, len(temperatures)):
            currTemp = temperatures[idx]
            while stack and currTemp > temperatures[stack[-1]]:
                updated = stack.pop()
                res[updated] = idx - updated
            stack.append(idx)
        
        return res
