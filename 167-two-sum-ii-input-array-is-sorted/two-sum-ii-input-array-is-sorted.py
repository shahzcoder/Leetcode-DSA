class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers) - 1
        while (head <= tail):
            pair_sum = numbers[head] + numbers[tail]

            if pair_sum < target:
                head += 1
            elif pair_sum > target:
                tail -= 1
            else :
                return [head + 1, tail + 1]
        
        return [-1,-1]
            
        



