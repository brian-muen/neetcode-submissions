class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        path = []

        if not digits:
            return res

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(idx):
            if idx == len(digits):
                res.append("".join(path))
                return

            curr_digit = digits[idx]
            
            for i in mapping[curr_digit]:
                path.append(i)
                backtrack(idx + 1)
                path.pop()


        backtrack(0)

        return res

        