class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.recursive(n, memo)
    
    def recursive(self, n, memo):
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            return 1
        if n < 0:
            return 0

        memo[n] = self.recursive(n - 1, memo) + self.recursive(n - 2, memo)
        return memo[n]