from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        left=1
        right=1
        for i in range(len(nums)):
            result.append(left)
            left*=nums[i]
        for i in range(len(nums)-1,-1,-1):# iterate from right to left
            result[i]*=right
            right*=nums[i]
        return result
    
s=Solution()
print(s.productExceptSelf([1,2,3,4]))
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         result=[]
#         for i in range(len(nums)):
#             newarr=np.delete(nums,i)
            
#             result.append(int(math.prod(newarr)))
#         return result
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         result=[]
#         for i in range(len(nums)):
#             prod=1
#             for j in range(len(nums)):
#                 if i!=j:
#                     prod*=nums[j]
#             result.append(prod)
#         return result