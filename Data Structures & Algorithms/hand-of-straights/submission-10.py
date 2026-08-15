class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        remaining = {}

        for i in hand:
            remaining[i] = remaining.get(i, 0) + 1

        hand.sort()
        for i in hand:
            if remaining[i] == 0:
                continue
            else:
                for value in range(i, i + groupSize):
                    if remaining.get(value, 0) == 0:
                        return False
                    else:
                        remaining[value] -= 1


        return True
    

