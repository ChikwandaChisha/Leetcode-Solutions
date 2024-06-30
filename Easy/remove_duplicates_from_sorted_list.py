from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0

        for right in range(1, len(nums)): 
            if nums[left] != nums[right ]: # if two numbers are not duplicates
                left += 1
                nums[left] = nums[right]              
                
        return left
            
