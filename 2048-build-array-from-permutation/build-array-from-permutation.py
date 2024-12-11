class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            num = nums[nums[i]]
            res.append(num)

        return res