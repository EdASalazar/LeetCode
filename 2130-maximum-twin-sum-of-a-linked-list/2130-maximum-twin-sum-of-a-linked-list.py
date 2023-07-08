# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        ans = 0
        while curr:
            arr.append(curr.val)
            curr = curr.next

        i = 0
        j = len(arr) - 1
        while i < j:
            newSum = arr[i] + arr[j]
            ans = max(ans, newSum)
            i += 1
            j -= 1

        

        return ans
        