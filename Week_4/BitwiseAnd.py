class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        count = 0
        while (n > m):
            n = n >> 1
            m = m >> 1
            count+= 1
        return m << count
        