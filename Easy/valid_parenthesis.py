class Solution:
    def isValid(self, s:str) -> bool:
        if len(s) % 2 != 0 : # check if string-length is odd or even
            return False
        brackets = {"}":"{", "]":"[", ")":"("}
        stack = []
        for i in s:
            if i in brackets: # if i is a closed bracket
                if stack and stack[-1] == brackets[i]: # check if stack is empty and if the last elemnt in the stack is complementary with thw current closed bracket
                    stack.pop() # pop out the last element
                else:
                    return False # return false if the two brackets are not compartible
            else:
                stack.append(i) # add to stack if it's an open bracket
    
        return len(stack) == 0 # check if stack if empty. If it is empty is means the open and closed brackets were even distributed in number


        