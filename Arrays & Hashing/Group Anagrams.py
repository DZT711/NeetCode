from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in range(len(strs)):
            countLetter=[0]*26
            for c in strs[i]:
                countLetter[ord(c)-ord('a')]+=1
            res[tuple(countLetter)].append(strs[i])
        return list(res.values())
s=Solution()
print(s.groupAnagrams(["eat","eat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat","fact"]))

#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         result=[]
#         freq_map = {}
#         for s in strs:
#             key = ''.join(sorted(s))
#             if key not in freq_map:
#                 freq_map[key] = []
#             freq_map[key].append(s)
#         for group in freq_map.values():
#             result.append(group)
#         return result

#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


#         orderedStrs = []
#         isOrdered = [False] * len(strs)
#         for i in range(len(strs)):
#             subArr = []
            
#             if not isOrdered[i]:
                
#                 for j in range(len(strs)):
#                     if sorted(strs[i])==sorted(strs[j]) :
#                         subArr.append(strs[j])
#                         isOrdered[j] = True
#                         isOrdered[i] = True
                        
#                 orderedStrs.append(subArr)

#         return orderedStrs