# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def reverse_in_order(node, acc_sum):
            if not node:
                return acc_sum
            
            acc_sum = reverse_in_order(node.right, acc_sum)
            acc_sum += node.val
            node.val = acc_sum
            acc_sum = reverse_in_order(node.left, acc_sum)
            
            return acc_sum
        
        reverse_in_order(root, 0)
        return root
    