class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        # if n is odd number
        if n % 2 == 1:
            result.append(0)

            # n // 2 calculate the mid 

        for i in range(1, (n // 2) + 1):
            result.append(i)
            result.append(-i)
        return result
