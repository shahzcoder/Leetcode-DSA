class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}
        for c in s:
            if c in mp:
                mp[c] += 1
            else:
                mp[c] = 1

        for i,c in enumerate(s):
            if mp[c] == 1:
                return i

        return -1

        