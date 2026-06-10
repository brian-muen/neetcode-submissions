class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1

        while p1 < p2:
            num1 = numbers[p1]
            num2 = numbers[p2]
            if num1 + num2 > target: 
                p2 -= 1
            elif num1 + num2 < target:
                p1 += 1
            else:
                return [p1 + 1, p2 + 1]
            
        