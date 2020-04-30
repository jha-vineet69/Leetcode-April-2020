# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self.existPath(root, arr, 0)
    
    def existPath(self,root, arr, index):
        if(root==None or index>=len(arr) or len(arr)==0):
            return False
        
        if((root.left==None and root.right==None) and (root.val==arr[index] and root.val==arr[len(arr)-1])):
            return True
        
        ans = False
        if(root.val == arr[index]):
            ans = self.existPath(root.left, arr, index+1) or self.existPath(root.right, arr, index+1)
            
        return ans
        