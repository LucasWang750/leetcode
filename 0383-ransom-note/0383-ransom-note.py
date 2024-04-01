class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = collections.Counter(magazine)
        hashmap2 = collections.Counter(ransomNote)
        
        print(hashmap)
        print(hashmap2)
        for i in hashmap2:
            if i in hashmap and hashmap[i] >= hashmap2[i]:
                continue
            else:
                return False
            # print(i)
        return True