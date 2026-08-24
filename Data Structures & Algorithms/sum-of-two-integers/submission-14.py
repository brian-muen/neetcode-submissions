class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        carry_bit = 0
        res = 0

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            curr_bit = a_bit ^ b_bit ^ carry_bit
            carry_bit = (a_bit & b_bit) | (a_bit & carry_bit) | (b_bit & carry_bit)

            if curr_bit:
                res |= (1 << i)

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res


                

