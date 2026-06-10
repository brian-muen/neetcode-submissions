class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        res.append(0)
        if n == 0: return res 
        else: res.append(1)
        diff = 2

        for i in range (2, n + 1):
            res.append(0)
            backp = i - diff
            if i - diff == diff: 
                diff = i
                backp = i - diff
            res[i] = 1 + res[backp]
        
        return res
            
            