class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_idx = 0
        left = [1]
        right = [1]
        result = []
        while left_idx < len(nums) - 1:
            left.append(nums[left_idx] * left[left_idx])
            right.append(nums[len(nums) - left_idx - 1] * right[left_idx])
            left_idx += 1
        
        right = list(reversed(right))
        
        for i in range(len(nums)):
            result.append(left[i] * right[i])
        
        return result