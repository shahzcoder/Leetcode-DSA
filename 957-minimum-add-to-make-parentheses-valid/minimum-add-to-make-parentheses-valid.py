class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        close = 0
        for c in s:
            if c == '(':
                open += 1
            elif c == ')' and open > 0:
                open -= 1
            else:
                close += 1 
        
        return open + close
            