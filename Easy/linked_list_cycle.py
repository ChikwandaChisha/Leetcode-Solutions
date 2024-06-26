# Definition for a singly linked list
class ListNode:
    def __init__(self, x) -> None:
         self.val = x
         self.next = None 

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head # have a fast and slow pointer set to head
        slow = head # if there is a cycle, the two pointers will meet at some point

        while fast != None and fast.next != None: # return false if fast or fast.next is None.
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    # Time complexity -> O(n)
    # Space complexity -> O(1)
    
    
    # HERE IS AN ALTERNATIVE SOLUTION
    
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set() # using set instead of list because list has search time complexity of O(n), set has O(1)
        pointer = head
        
        while pointer != None: # if pointer is None, there's no cycle
            if pointer in node_set:
                return True
            else:
                node_set.add(pointer)
                pointer = pointer.next
        
        return False
    # Time complexity -> O(n)
    # Space complexity -> O(n)
                