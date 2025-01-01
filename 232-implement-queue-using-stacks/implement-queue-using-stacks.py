class MyQueue:

    def __init__(self):
        self.input_stack = []  # Stack for pushing elements
        self.output_stack = []  # Stack for popping/peeking elements

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        self._move_input_to_output()
        return self.output_stack.pop()

    def peek(self) -> int:
        self._move_input_to_output()
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack

    def _move_input_to_output(self) -> None:
        if not self.output_stack:  # Only move if output stack is empty
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()