class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        
        left = 0
        right = 0
        new_s = ""
        while right < len(s):
            if s[right] == " ":
                if left == right:
                    left = right + 1
                else:
                    new_s = s[left:right] + " " + new_s
                    left = right + 1
            right += 1
        new_s = s[left:right] + " " + new_s
        return new_s[:len(new_s)-1]