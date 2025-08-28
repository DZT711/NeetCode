from typing import List 
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return [num for num, _ in counts.most_common(k)]
        
    
s=Solution()
print(s.topKFrequent([7,7],1))