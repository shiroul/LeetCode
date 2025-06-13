class Solution:
    def reverseBits(self, n: int) -> int:
        s = '{:032b}'.format(n)
        s = s[::-1]
        return int(s, 2)