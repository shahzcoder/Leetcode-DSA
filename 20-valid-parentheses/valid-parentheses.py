class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchingBrackets = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in matchingBrackets.values():
                stack.append(char)
            elif char in matchingBrackets.keys():
                if not stack or stack[-1] != matchingBrackets[char]:
                    return False
                
                stack.pop()

            else:
                return False
        
        return len(stack) == 0
