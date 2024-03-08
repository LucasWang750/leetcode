class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = -1
        digits[index] += 1
        carryOver = 1 if digits[index] == 10 else 0
        if carryOver == 1:
            digits[index] = 0
        index = -2
        while carryOver == 1 and -index <= len(digits):
            digits[index] += carryOver
            carryOver = 1 if digits[index] == 10 else 0
            if carryOver == 1:
                digits[index] = 0
            index -= 1
            
        if carryOver == 1:
            digits.insert(0, 1)
            
        return digits