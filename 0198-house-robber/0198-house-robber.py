class Solution:
    
    def rob(self, nums: List[int]) -> int:
        prev, prevprev = 0, 0 
        for val in nums:
            best = max(val + prevprev, prev)
            prev, prevprev = best, prev
        
        return max(prev, prevprev)