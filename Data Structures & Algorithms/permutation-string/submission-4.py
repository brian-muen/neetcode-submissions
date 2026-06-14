from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)

        hash_map = {}

        if len(s1) > len(s2): 
            return False

        for i in range(len(s1)):
            curr_char = s2[i]
            if curr_char in hash_map:
                hash_map[curr_char] += 1
            else:
                hash_map[curr_char] = 1

        if hash_map == target:
            return True

        l = 0
        r = len(s1)

        while r < len(s2):
            removing = s2[l]
            if hash_map[removing] == 1:
                del hash_map[removing]
            else:
                hash_map[removing] -= 1

            adding = s2[r]
            if adding in hash_map:
                hash_map[adding] += 1
            else: 
                hash_map[adding] = 1

            if hash_map == target:
                return True
            
            l += 1;
            r += 1;
        
        return False

