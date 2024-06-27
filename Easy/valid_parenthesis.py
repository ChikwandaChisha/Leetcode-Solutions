class Solution:
    def isValid(self, s:str) -> bool:
        open_brac_map = {'[':']', '{':'}', '(':')'} # create hashmaps to map a bracket to its complementary bracket
        closed_brac_map = {']':'[', '}':'{', ')':'('}
        open_stack = [] # create two stacks to pop off from
        closed_stack = []
        
        for c in s:
            if c in open_stack: # add to open_stack if the bracket is an open one
                open_stack.append(c)
            elif c in closed_stack: # add to closed_stack if the bracket is a closec one
                closed_stack.append(c)
            else:
                return False # return False if the character is not a bracket
        
        if len(open_stack) != len(closed_stack): # if the two stacks are not the same length, return False
            return False
        
        for i in range(len(open_stack), -1): # loop through open_stack (or closed_stack) starting with the last index
            if open_brac_map[open_stack.pop(i)] != closed_stack.pop(i): # if the last item in the open_stack is not complementary to the last in the closed_stack, it's not valid
                return False
        
        return True
    
    
        # if len(s) % 2 != 0 :
        #     return False
        # brackets = {"}":"{", "]":"[", ")":"("}
        # stack = []
        # for i in s:
        #     if i in brackets:
        #         if stack and stack[-1] == brackets[i]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(i)
    
        # if len(stack) == 0:
        #     return True
        # return False

        