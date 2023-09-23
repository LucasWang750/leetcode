class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left,mid,right = [],[],[]
        
        for num in nums:
            #switch left to bigger cuz k-biggest
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)
            else:
                mid.append(num)
        
        if k <= len(left):
            return Solution.findKthLargest(self, left, k)

        if len(left) + len(mid) < k:
            return Solution.findKthLargest(self, right, k - len(left) - len(mid))
        
        return pivot
            