from typing import List 
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = {}
        freq=[[]for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
s=Solution()
print(s.topKFrequent([7,7],1))
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         result = []
#         counts = Counter(nums)
#         for num, _ in counts.most_common(k):
#             result.append(num)
#         return result
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counts = Counter(nums)
#         return [num for num, _ in counts.most_common(k)]