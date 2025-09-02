class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        else:
            freq=[[0]*26]
            for i in range(len(s)):
                freq[0][ord(s[i])-ord('a')]+=1 #Cú pháp này thường dùng để biến một ký tự thường ('a'–'z') thành chỉ số từ 0 đến 25, rất hữu ích khi làm việc với mảng đếm tần suất (frequency array) dài 26
                freq[0][ord(t[i])-ord('a')]-=1
            for i in range(26):
                if freq[0][i]!=0:
                    return False 
            else:
                return True
s=Solution()
print(s.isAnagram("anagram", "nagaram"))  # True
print(s.isAnagram("lam", "fam"))  
print(s.isAnagram("lam", "lam1"))  

#     def isAnagram(self, s: str, t: str) -> bool:

#         return sorted(s)==sorted(t)