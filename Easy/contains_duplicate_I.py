class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums)) # a set does not contain duplicates.
    
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups = set()     # set does not allow duplicates               
        for num in nums:
            if num in dups:  # set has O(1) "find" time complexity 
                return True      
            else:
                dups.add(num)
        return False