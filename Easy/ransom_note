class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_map = {}
        for c in magazine: # add magazine characters to a hashmap
            if c in mag_map:
                mag_map[c] += 1
            else:
                mag_map[c] = 1

        for k in ransomNote: # check if the key is in mag_map and does not appear more than mag_map[key] times
            if k not in mag_map:
                return False
            elif mag_map[k] == 0:
                return False
            mag_map[k] -= 1
        return True

        # Time complexity -> O(n+m), where m = len(magazine) and n = len(ransomNote) 
        # Space complexity -> O(1), the map has a max of 26 alphabet characters.


        




        