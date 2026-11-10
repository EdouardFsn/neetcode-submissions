# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        size =0
        pointer = head
        while(pointer):
            pointer = pointer.next
            size += 1
        prev = dummy
        pointer2 = head
        for i in range(size - n):
            prev =  pointer2
            pointer2 = pointer2.next
        prev.next = pointer2.next
        return dummy.next
        
            

        