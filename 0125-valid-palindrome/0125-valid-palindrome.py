class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = list(map(lambda ch: ch.lower() ,filter(lambda ch: ch.isalnum(), s)))
        
        return result == list(reversed(result))