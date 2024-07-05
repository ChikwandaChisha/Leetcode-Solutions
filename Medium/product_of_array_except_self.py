class Solution:
    def productExceptSelf(self, nums:list[int]) -> list[int]:
        l_nums = len(nums)
        res = [1] * l_nums
        prefix = 1 # represents the product of numbers before a numer
        for i in range(l_nums):
            res[i] = prefix 
            prefix *= nums[i] # update prefix as you traverse through the list
        
        suffix = 1 # product of numbers after a number
        for j in range(l_nums - 1, -1, -1):
            res[j] *= suffix # update number at j by multiplying by the suffix
            suffix *= nums[j]
        
        return res
    # Time complexity -> O(n)
    # Space complexity -> O(1), assuming the output does not account for space complexity