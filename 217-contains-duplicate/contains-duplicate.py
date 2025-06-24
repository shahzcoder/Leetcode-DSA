from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for num in nums:
            if num in count:
                count[num] += 1
                return True
            else:
                count[num] = 1
            
        return False