# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root:
            return res
        q=deque()

        q.append(root)
      
        while q:
            levelLen=len(q)
            levelItem=None
            for i in range(levelLen):
               node=q.popleft()
               print(node)
               if node:
                   levelItem=node.val
                   q.append(node.left)
                   q.append(node.right)
            
            if levelItem!=None:
                res.append(levelItem)

        return res