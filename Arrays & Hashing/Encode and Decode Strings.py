from typing import List
class Solution:

    def __init__(self):
        self.lengths: List[int] = []

    def encode(self, strs: List[str]) -> str:
        self.lengths = [len(w) for w in strs]
        return ''.join(w * 2 for w in strs)

    def decode(self, s: str) -> List[str]:
        res: List[str] = []
        i = 0
        for L in self.lengths:
            res.append(s[i:i+L])   # lấy nửa đầu
            i += 2 * L             # bỏ qua cả "wordword"
        return res
s=Solution()
x=s.encode(["neet","code","love","you"])
print(x)
print(s.decode(x))
y=s.encode(["we","say",":","yes"])
print(y)
print(s.decode(y))