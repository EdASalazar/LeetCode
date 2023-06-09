# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
            if left == right or not head.next:
                return head
            
            current, prev, pos = head, None, 1
            while current.next and pos < left:
                prev, current = current, current.next
                pos += 1
            
            end_of_left = prev
            end_of_mid = current
            while pos < right:
                to_do_next, current.next, prev = current.next, prev, current
                current = to_do_next
                pos += 1
            
            if left == 1:
                head = current
            
            else: 
                end_of_left.next = current
            end_of_mid.next, current.next = current.next, prev
            return head
