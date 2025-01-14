class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for operand in tokens:

            if operand == "+":
                stack.append(stack.pop() + stack.pop())
            elif operand == "-":
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            elif operand == "*":
                stack.append(stack.pop() * stack.pop())
            elif operand == "/":
                second, first = stack.pop(), stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(operand))
            
        return stack[0]