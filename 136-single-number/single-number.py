class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        newNums = set(nums)

        for i in newNums:
            if nums.count(i) == 1:
                return i
        

        