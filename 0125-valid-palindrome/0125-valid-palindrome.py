class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for i in s:
            if 97 <= ord(i.lower()) <= 122 or 48 <= ord(i.lower()) <= 57:
                result.append(i.lower())
        return result == list(reversed(result))