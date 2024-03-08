class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        metLetter = False
        length = 0
        for i in s[::-1]:
            if i ==  " " and metLetter == True:
                return length
            if i.isalpha():
                length += 1
                metLetter = True
        return length