class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        dup = [0] * length

        for i in range(length):
            if i + k < length:
                dup[i+k] = nums[i]
            else:
                dup[ (i+k) % length] = nums[i]
        
        nums[:] =  dup
        
        

        """
        Do not return anything, modify nums in-place instead.
        """
        