class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        dups = set()                    # set has O(1) "find" time complexity 
        for num in nums:
            if num in dups:
                return True             # duplicate if num is in dups

            else:
                dups.add(num)
        return False