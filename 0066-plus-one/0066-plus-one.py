class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = -1
        carryOver = 1
        while -index <= len(digits):
            digits[index] += carryOver
            carryOver = 1 if digits[index] == 10 else 0
            if carryOver == 1:
                digits[index] = 0
            index -= 1
        if carryOver == 1:
            digits.insert(0, 1)
            
        return digits