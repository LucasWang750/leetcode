class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        
        @lru_cache(maxsize=None)
        def recur(idx1, idx2):
            if len(text1) == idx1 or len(text2) == idx2:
                return 0

            idx = text2.find(text1[idx1], idx2)
            subproblem1 = 0
            if (idx != -1):
                subproblem1 = 1 + recur(idx1+1, idx+1)
            subproblem2 = recur(idx1+1, idx2)
            
            return max(subproblem1, subproblem2)
        return recur(0, 0)