class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        # maximum difference that is positive
        val = -1
        for i in range(len(nums)):
            for j in range(i , len(nums)):
                if nums[j] - nums[i] > 0:
                    val = max(val, nums[j] - nums[i])
        return val
        