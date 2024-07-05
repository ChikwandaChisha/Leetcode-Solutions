# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = []
        queue.append(root)
        res = []
        res.append(root.val)
        while queue:
            total = 0
            n = 0
            temp = [] # temporary queue that keeps track of the nodes at each level
            
            while queue: # whilst on one level
                curr = queue.pop()
                if curr.left:
                    temp.append(curr.left)
                    total += curr.left.val
                    n += 1
                if curr.right:
                    temp.append(curr.right)
                    total += curr.right.val
                    n += 1
            queue = temp # equate temp to queue and later rest temp
            if n != 0:
                res.append(total/n)
        return res
            