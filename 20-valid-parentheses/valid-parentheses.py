class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = "({["
        closing = ")}]"
        pairs = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if not stack or stack.pop() != pairs[char]:
                    return False
        
        return len(stack) == 0