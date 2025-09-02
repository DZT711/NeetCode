class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        # left=0 , right=len(s)-1
        # isalnum() mean check if that char is a number or a letter
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
s=Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome("lo                     l"))
print(s.isPalindrome("loop                     pool"))
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         filtered_chars = [char.lower() for char in s if char.isalnum()]
#         return filtered_chars == filtered_chars[::-1]