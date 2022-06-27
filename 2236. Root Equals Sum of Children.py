# Solution du second problème : (2236. Root Equals Sum of Children)
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def checkTree(self, root):
        return (root.val == (root.left.val + root.right.val))
        