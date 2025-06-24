class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # output = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        look = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in look:
                return [look[complement], i]
            look[nums[i]] = i


