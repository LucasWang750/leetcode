# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        bad = left + (right - left) // 2

        while left < right:
            
            if isBadVersion(bad):
                right = bad
            else:
                left = bad + 1
                
            bad = left + (right - left) // 2

        return bad