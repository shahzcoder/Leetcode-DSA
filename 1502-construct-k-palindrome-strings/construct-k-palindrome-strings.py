from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        
        charCount = Counter(s)
        oddCount = sum(1 for count in charCount.values() if count % 2 != 0)

        return oddCount <= k
