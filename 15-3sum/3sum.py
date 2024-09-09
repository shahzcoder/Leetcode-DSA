class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to use the two-pointer technique efficiently
        output = []
        
        for i in range(len(nums) - 2):  # Outer loop over the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements for the first position
            
            left, right = i + 1, len(nums) - 1  # Set left and right pointers
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers to avoid duplicates for the second and third numbers
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the second number (left pointer)
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    # Skip duplicates for the third number (right pointer)
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1  # Increase sum by moving left pointer to the right
                else:
                    right -= 1  # Decrease sum by moving right pointer to the left
        
        return output