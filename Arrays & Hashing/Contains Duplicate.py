from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
    
sol = Solution()
print(sol.hasDuplicate([1,2,3,3]))
print(sol.hasDuplicate([1,2,3,4]))  