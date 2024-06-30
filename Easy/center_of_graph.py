from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # the center will be present in atleast two sets, assuming there is no repetition
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]
        