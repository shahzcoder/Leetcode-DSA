class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for element in pushed:
            stack.append(element)
            while stack and stack[-1] == popped[j]:
                j += 1
                stack.pop()
        return len(stack) == 0

