class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}

        for idx, letter in enumerate(s):
            pos[letter] = idx

        res = []


        l = 0
        r = 0

        for idx, letter in enumerate(s):
            if pos[letter] == idx and r == idx:
                res.append(r - l + 1)
                l = min(idx + 1, len(s) - 1)
                r = min(idx + 1, len(s) - 1)
            else:
                r = max(pos[letter], r)

        return res
            



        