class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        result = -1
        passes = len(nums) // 2
        left, right = 0, len(nums) - 1
        i = 0
        while i <= passes:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            i += 1
        
        return result