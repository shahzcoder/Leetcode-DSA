class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs = 0
        count = 0

        for i in range(len(s)):
            if s[i] == 'E':
                count += 1
            else:
                count -= 1
            
            if chairs < count:
                chairs += 1
        return chairs