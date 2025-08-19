from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        orderedStrs = []
        isOrdered = [False] * len(strs)
        for i in range(len(strs)):
            subArr = []
            
            if not isOrdered[i]:
                
                for j in range(len(strs)):
                    if sorted(strs[i])==sorted(strs[j]) :
                        subArr.append(strs[j])
                        isOrdered[j] = True
                        isOrdered[i] = True
                        
                orderedStrs.append(subArr)

        return orderedStrs
s=Solution()
print(s.groupAnagrams(["eat","eat"]))
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat","fact"]))