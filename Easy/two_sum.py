class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        dic = {} #initializing dictionary
        
        for i in range(len(nums)):
            dic[target - nums[i]] = i   #mapping difference to index
            
        for j in range(len(nums)):
            if nums[j] in dic and j != dic[nums[j]]: #check if j != i to avoid repetition
                return[dic[nums[j]], j]  #return i and j
        
        return []
        