# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if q == None and p == None :
            return True 
        elif p != None and q != None and p.val == q.val:
            return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
        else : return False
        
    