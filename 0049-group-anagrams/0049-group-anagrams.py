class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hashmap = {}
#         for i in strs:
#             sorted_str = "".join(sorted(i))
#             if sorted_str in hashmap:
#                 hashmap[sorted_str].append(i)
#             else:
#                 hashmap[sorted_str] = [i]
        
        
#         return list(hashmap.values())

        ans = collections.defaultdict(list)
        for i in strs:
            ans[''.join(sorted(i))].append(i)
        return ans.values()