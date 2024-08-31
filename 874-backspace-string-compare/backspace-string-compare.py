class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove_character(s):
            stack = []
            for char in s:
                if char == "#" and stack:
                    stack.pop()
                elif char != "#":
                    stack.append(char)
            return stack

        return remove_character(s) == remove_character(t)
