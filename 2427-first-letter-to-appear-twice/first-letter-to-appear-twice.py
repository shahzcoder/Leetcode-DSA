class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = []
        for char in s:
            if char in seen:
                return char
            else:
                seen.append(char)