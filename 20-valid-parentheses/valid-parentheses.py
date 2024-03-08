class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                b = stack.pop()
                if c != brackets[b]:
                    return False

        return True if not stack else False
