class Solution:
    def validPalindrome(self, s:str) -> bool:
        l = 0
        r = len(s) - 1
        del_count = 0
        
        while l < r:
            if del_count > 1:
                return False
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            else:
                if s[l+1] == s[r]:
                    l += 1
                    count += 1
                elif s[l] == s[r-1]:
                    r -= 1
                    count += 1
        
        return True
        