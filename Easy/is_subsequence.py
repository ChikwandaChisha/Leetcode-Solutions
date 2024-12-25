class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S_BOUND = len(s)
        T_BOUND = len(t)

        s_pointer = t_pointer = 0

        while s_pointer < S_BOUND and t_pointer < T_BOUND: 
            if s[s_pointer] == t[t_pointer]:  # increase s_pointer if the characters at t_pointer and s_pointer are the same
                s_pointer += 1
            t_pointer += 1
        
        return S_BOUND == s_pointer