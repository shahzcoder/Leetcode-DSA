class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        for i in s:
            count[i] += 1

        for j in t:
            count[j] -= 1

        for val in count.values():
            if val != 0:
                return False
        
        return True

