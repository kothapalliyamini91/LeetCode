# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, sum):
        if not root: return  False
        sum-= root.val
        if not root.left and not root.right and sum==0: return True
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
            




        