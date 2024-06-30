# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: # return list2 if list1 is empty
            return list2
        if not list2: # return list1 if list2 is empty
            return list1

        if list1.val > list2.val: 
            head = list2 # head pointer point to list2
            list2 = list2.next # list2 pointer point to the next node
        else:
            head = list1 # head pointer point to list1
            list1 = list1.next # list1 pointer point to next node
        
        curr = head # curr pointer ensures head pointer is unchanged while updating it
       
        while list1 and list2: # as long as none is null
            if list1.val < list2.val:
                curr.next = list1 
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next # curr pointer points to the next one
        
        if list2: # add the remainder of list2 if it's not empty
            curr.next = list2
        elif list1: # add the remainder of list1 if it's not empty
            curr.next = list1
        
        return head # return head and not curr because curr could be pointing at the last node of somewhere in the middle
