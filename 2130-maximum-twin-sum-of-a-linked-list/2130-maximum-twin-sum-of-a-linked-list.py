# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        maxSum = 0
        
        while curr:
            arr.append(curr.val)
            curr = curr.next

        i = 0
        j = len(arr) - 1
        while i < j:
            newSum = arr[i] + arr[j]
            maxSum = max(maxSum, newSum)
            i += 1
            j -= 1

        

        return maxSum
        