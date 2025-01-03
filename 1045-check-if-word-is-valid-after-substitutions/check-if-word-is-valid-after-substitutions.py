class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 3:
            return False

        stack = []

        for char in s:
            stack.append(char)

            if ''.join(stack[-3:]) == 'abc':
                stack[-3:] = []
        
        return not stack
