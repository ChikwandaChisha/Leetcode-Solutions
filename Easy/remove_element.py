from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums[i], nums[len(nums) - 1] = nums[len(nums) - 1], nums[i] # swap number with number at last index
                nums.pop()
            else:
                i += 1 # increase i only if the first statement doesn't stand incase the last element in nums is also val

        return len(nums)
        # Time complexity -> O(n), Space complexity -> O(1)