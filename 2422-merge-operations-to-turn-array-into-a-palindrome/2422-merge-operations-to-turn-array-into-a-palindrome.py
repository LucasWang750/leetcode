class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        
        left = 0
        right = len(nums) - 1
        
        count = 0
        
        while left < right:
            
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] > nums[right]:
                count += 1
                nums[right - 1] = nums[right - 1] + nums[right]
                right -= 1
            else: 
                count += 1
                nums[left + 1] = nums[left + 1] + nums[left]
                left += 1
        
        return count