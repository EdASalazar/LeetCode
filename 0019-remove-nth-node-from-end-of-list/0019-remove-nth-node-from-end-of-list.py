# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        

        dummy = ListNode(0)
        dummy.next = head 

        slow, fast = dummy, dummy
        
        for _ in range(n):
            fast = fast.next
            print(fast, 'slow')
                
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
            print(fast, 'fast')
        
        slow.next = slow.next.next
     
        
        return dummy.next
            
            