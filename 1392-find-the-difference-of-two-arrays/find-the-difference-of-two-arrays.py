class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        answer = []
        nums3 = nums1.difference(nums2)
        answer.append(nums3)
        nums4 = nums2.difference(nums1)
        answer.append(nums4)
        
        return answer

