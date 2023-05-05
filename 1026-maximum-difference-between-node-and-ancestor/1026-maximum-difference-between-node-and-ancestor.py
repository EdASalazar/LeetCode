# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.result = 0
    
        
            
        
        
        def findDiff(node, max_diff, min_diff):
            if not node:
                return
            self.result = max(self.result, (abs(max_diff - node.val)), (abs(min_diff - node.val)))
            max_diff = max(max_diff, node.val)
            min_diff = min(min_diff, node.val)
            findDiff(node.left, max_diff, min_diff)
            findDiff(node.right, max_diff, min_diff)

        findDiff(root, root.val, root.val)
  
        return self.result
            