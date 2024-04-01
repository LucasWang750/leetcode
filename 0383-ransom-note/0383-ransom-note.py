class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = collections.Counter(magazine)
        hashmap2 = collections.Counter(ransomNote)
        for i in hashmap2:
            if i in hashmap and hashmap[i] >= hashmap2[i]:
                continue
            else:
                return False
        return True