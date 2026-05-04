class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s, count_t = {} , {}

        for c in s:
            if c in count_s:
                count_s[c] += 1
            else:
                count_s[c] = 1

        for a in t:
            if a in count_t:
                count_t[a] += 1
            else: 
                count_t[a] = 1

        return count_s == count_t