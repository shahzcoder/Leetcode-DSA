class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0,0
        for i in nums:
            if count == 0:
                res = i
            if res == i:
                count += 1
            else:
                count -= 1
        return res
        # space O(1) time O(n)

    