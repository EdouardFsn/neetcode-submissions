# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        group_prev = dummy  
        test = self.test_next_k(dummy, k)
        while (test != None):
            group_next = test.next              
            first = group_prev.next             
            group_prev.next = self.reversekelem(first, k, group_next)
            group_prev = first                  
            test = self.test_next_k(group_prev, k)
        return dummy.next



    def reversekelem(self, head: Optional[ListNode], k: int, after: Optional[ListNode]) -> Optional[ListNode]:
        prev = after         
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev



    def test_next_k(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        for i in range(k):
            if head.next:
                head = head.next
            else: 
                return None
        return head