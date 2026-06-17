class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for idx, char in enumerate(s):
            left, right = idx, idx
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if len(s[left:right+1]) > len(res):
                        res = s[left:right+1]
                else:
                    break
                left -= 1
                right += 1

        
            right = idx + 1
            left = idx
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if len(s[left:right+1]) > len(res):
                        res = s[left:right+1]
                else:
                    break
                left -= 1
                right += 1

        return res