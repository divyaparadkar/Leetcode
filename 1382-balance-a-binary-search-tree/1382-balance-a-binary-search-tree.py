# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder_traversal(root):
            result = []
            if root:
                result = inorder_traversal(root.left)
                result.append(root.val)
                result = result + inorder_traversal(root.right)
            return result

        def sorted_array_to_bst(nums):
            if not nums:
                return None

            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = sorted_array_to_bst(nums[:mid])
            node.right = sorted_array_to_bst(nums[mid+1:])
            
            return node

        sorted_nodes = inorder_traversal(root)
        return sorted_array_to_bst(sorted_nodes)
        