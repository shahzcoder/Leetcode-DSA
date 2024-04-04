class Solution:
    def maxDepth(self, s: str) -> int:
        counter, maxCounter = 0,0
        for i in range(len(s)):
            if s[i] == "(":
                counter += 1
                if maxCounter < counter:
                    maxCounter = counter
            if s[i] == ")":
                counter -= 1
        return maxCounter                