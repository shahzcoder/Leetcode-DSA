class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums1 = set(nums)
        lst = []
        for i in range(1,len(nums) + 1):
            if i not in nums1:
                lst.append(i)
        return lst

