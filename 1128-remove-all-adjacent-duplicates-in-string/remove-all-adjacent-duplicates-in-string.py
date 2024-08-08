class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for c in s:
            if stk:
                if stk[-1] == c:
                    stk.pop()
                else:
                    stk.append(c)
            else:
                stk.append(c)

        
        return ''.join(stk)