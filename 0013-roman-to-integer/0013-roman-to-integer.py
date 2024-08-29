class Solution:
    def romanToInt(self, s: str) -> int:
        
        last_char = s[0]
        total = 0
        
        for i in s:
            if i == 'I':
                total += 1
            if i == 'V':
                total += 5
                if last_char == 'I':
                    total -= 2
            if i == 'X':
                total += 10
                if last_char == 'I':
                    total -= 2
            if i == 'L':
                total += 50
                if last_char == 'X':
                    total -= 20
            if i == 'C':
                total += 100
                if last_char == 'X':
                    total -= 20
            if i == 'D':
                total += 500
                if last_char == 'C':
                    total -= 200
            if i == 'M':
                total += 1000
                if last_char == 'C':
                    total -= 200
            last_char = i
        return total