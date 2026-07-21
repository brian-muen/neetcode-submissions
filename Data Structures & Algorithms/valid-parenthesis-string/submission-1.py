class Solution:
    def checkValidString(self, s: str):

        left_stack = deque()
        wild_stack = deque()

        for i , char in enumerate(s):
            if char == '(':
                left_stack.append(i)
            elif char == '*':
                wild_stack.append(i)
            else:
                if left_stack:
                    left_stack.pop()
                elif wild_stack:
                    wild_stack.popleft()
                else:
                    return False
        indexLeft = 0
        indexWild = 0
        if not wild_stack and left_stack:
            return False
        
        if len(wild_stack) < len(left_stack):
            return False

        while left_stack and wild_stack:
            indexLeft = left_stack.pop()
            indexWild = wild_stack.pop()
            if indexWild < indexLeft:
                return False
       
        return True
   




