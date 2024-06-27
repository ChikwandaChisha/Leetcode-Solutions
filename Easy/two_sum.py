class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        dic = {}  # initializing dictionary

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic:
                return [dic[complement], i]  # return indices if complement is found
            dic[nums[i]] = i  # map the current number to its index

        return []
            