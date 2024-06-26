class Solution:
    def validPalindrome(x: int) -> bool:
        if x < 0: #check if x is negative
            return False
        num = str(x) # cast the integer to a string
        left = 0
        right = len(num) - 1
        
        while left < right: #left and right do not need to cross or point at the same number
            if num[left] == num[right]: # if a pair is valid, increase left pointer and decrease right pointer
                left += 1
                right -= 1
            else:
                return False
        return True
            