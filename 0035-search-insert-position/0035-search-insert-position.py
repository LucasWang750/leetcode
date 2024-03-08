class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        left = 0
        right = len(nums)
        mid = (left + right) // 2
        while left < right:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
            mid = (left + right) // 2  
        return mid