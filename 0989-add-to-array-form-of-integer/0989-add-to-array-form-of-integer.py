class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        index = -1
        carryOver = k
        while -index <= len(num):
            num[index] += carryOver
            carryOver = num[index] // 10
            num[index] = num[index] % 10
            index -= 1
            
        while carryOver > 0:
            num.insert(0, carryOver % 10)
            carryOver = carryOver // 10
        return num
        