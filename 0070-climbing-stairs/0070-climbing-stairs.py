class Solution:
    def climbStairs(self, n: int) -> int:
        
        @functools.lru_cache(maxsize=128)
        def ways(n):
            if n == 2:
                return 2
            if n == 1:
                return 1
            else:
                plusOne = ways(n-1)
                plusTwo = ways(n-2)
                return plusOne+plusTwo
        return ways(n)