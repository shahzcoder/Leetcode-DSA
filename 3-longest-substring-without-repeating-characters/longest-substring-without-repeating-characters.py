class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = 0
        sb = 0

        for r in range(len(s)):
            if s[r] in hashmap:
                l = max(l, hashmap[s[r]] + 1)
                
            hashmap[s[r]] = r
            sb = max(sb,r - l + 1)

        return sb