'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return self.nodeSum(root)[1]
        return 0
        
    def nodeSum(self, node):
        l , r = 0, 0
        ls, rs = None, None
        if node.left:
            l, ls = self.nodeSum(node.left)
            l = max(l, 0)
        if node.right:
            r, rs = self.nodeSum(node.right)
            r = max(r, 0)
        return node.val + max(l, r), max(node.val + l + r, ls, rs)
        