from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        left,right = 0,len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]==target:
                res.append(left+1)
                res.append(right+1)
                break
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1
        return res
s=Solution()
print(s.twoSum([7,2,7,11,15],9))

#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # result=[]
        # for i in numbers:
        #     j=target-i
        #     if j in numbers and j!=i:
        #         if numbers.index(i)<numbers.index(j):
        #             result.append(numbers.index(i)+1)   # require index 1 < index 2 and their values cannot be equal
        #             result.append(numbers.index(j)+1)   # require output use real indexes
        #         else:
        #             result.append(numbers.index(j)+1)
        #             result.append(numbers.index(i)+1)   
        #         break
        # return result   