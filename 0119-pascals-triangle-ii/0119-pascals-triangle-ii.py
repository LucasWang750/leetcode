class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [1] * (rowIndex + 1)
        
        for i in range(rowIndex + 1):
            temp = arr[:]
            for j in range(1, i):
                temp[j] = arr[j-1] + arr[j]
            arr = temp[:]
        return arr
        