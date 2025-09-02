from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestLength=0
        numSet=set(nums)
        for num in numSet:
            if num-1 not in numSet:
                length=0
                while num+length in numSet:
                    length+=1
                longestLength=max(longestLength,length)

        return longestLength
        
s=Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive([1,2,0,1,4,5,6,7]))
print(s.longestConsecutive([0,3,2,5,4,6,1,1]))
print(s.longestConsecutive([]))

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if len(nums)==0:
#             return 0
#         longestLength=0
#         nums=sorted(set(nums))
#         sequence=set()
#         sequence.add(nums[0])
#         for i in range(1,len(nums)):
#             if nums[i]==nums[i-1]+1:
#                 sequence.add(nums[i])
#             else:
#                 longestLength=max(longestLength,len(sequence))
#                 sequence=set()
#                 sequence.add(nums[i])
#         longestLength=max(longestLength,len(sequence))         
#         return longestLength