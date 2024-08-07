class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = [""]    
        for c in s:
            if c == '(':
                stk.append("")
            elif c == ')':
                top = stk.pop()[::-1]
                stk[-1] += top
            else:
                stk[-1] += c

        return stk[0]