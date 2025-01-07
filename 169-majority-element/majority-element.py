class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        records = {}
        for num in nums:
            if num in records:
                records[num]+=1
            else:
                records[num] = 1
            if records[num]>len(nums)//2:
                return num
        # n = len(nums) // 2
        # m = defaultdict(int)
        # for num in nums:
        #     m[num] += 1

        # for key,value in m.items():
        #     if value > n:
        #         return key
        
        # return 0 
    