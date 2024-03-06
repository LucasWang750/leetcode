class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        first = strs[0]
        index = 0
        while True:
            for i in range(len(strs)):
                if index == len(strs[i]) or first[index] != strs[i][index]:
                    return ans
            ans += first[index]
            index += 1
            
        return ans 
