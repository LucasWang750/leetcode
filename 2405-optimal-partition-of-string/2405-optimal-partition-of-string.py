class Solution:
    def partitionString(self, s: str) -> int:
        #greedy
        lastSeen = [-1] * 26
        count = 1
        substringStartIndex = 0 
        for i in range(len(s)):
            if lastSeen[ord(s[i]) - ord('a')] >= substringStartIndex:
                count += 1
                substringStartIndex = i
            lastSeen[ord(s[i]) - ord('a')] = i
        return count
        
        
        