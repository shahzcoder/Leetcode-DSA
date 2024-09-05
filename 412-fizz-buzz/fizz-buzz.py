class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.insert(i, "FizzBuzz")
            elif i % 3 == 0:
                answer.insert(i , "Fizz")
            elif i % 5 == 0:
                answer.insert(i , "Buzz")
            else:
                answer.insert(i, str(i))
        
        return answer


