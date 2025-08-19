class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
s=Solution()
print(s.isAnagram("anagram", "nagaram"))  # True
print(s.isAnagram("lam", "fam"))  # True
print(s.isAnagram("lam", "lam1"))  