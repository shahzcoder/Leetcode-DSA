class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        array = []
        lf_space = 0
        for i in range(len(s)):
            if lf_space < len(spaces) and i == spaces[lf_space]:
                array.append(" ")
                lf_space += 1
            array.append(s[i])
        return "".join(array)