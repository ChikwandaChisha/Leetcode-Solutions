class Solution:
    def validPalindrome(self, s:str) -> bool:
        def substringPalindrome(sub:str) -> bool: # create a helper function to check if the substring is a palindrome
            sub_l = 0
            sub_r = len(sub) - 1
            while sub_l < sub_r:
                if sub[sub_l] == sub[sub_r]:
                    sub_l += 1
                    sub_r -= 1
                else:
                    return False
            return True

        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] == s[r]: # update l and r if the two characters are equal
                l += 1
                r -= 1
            else:
                return substringPalindrome(s[l:r]) or substringPalindrome(s[l+1:r+1])
        return True
    

        