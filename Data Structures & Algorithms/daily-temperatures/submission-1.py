class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                updated = stack.pop()
                res[updated] = idx - updated
            stack.append(idx)
        
        return res
