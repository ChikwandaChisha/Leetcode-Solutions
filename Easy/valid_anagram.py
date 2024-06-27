class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for i in range(len(s)):
            if s[i] in dict_s:
                dict_s[s[i]] += 1
            elif s[i] not in dict_s:
                dict_s[s[i]] = 1
            if t[i] in dict_t:
                dict_t[t[i]] += 1
            elif t[i] not in dict_t:
                dict_t[t[i]] = 1
        
        return dict_s == dict_t