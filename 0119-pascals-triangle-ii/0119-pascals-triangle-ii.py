class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [1] * (rowIndex + 1)
        
        for i in range(rowIndex + 1):
            temp = arr[:]
            left = 1
            right = i - 1
            while left <= right:
                temp[left] = arr[left-1] + arr[left]
                temp[right] = temp[left]
                left += 1
                right -= 1
            # for j in range(1, i):
            #     temp[j] = arr[j-1] + arr[j]
            arr = temp[:]
        return arr
        