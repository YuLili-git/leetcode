#给定一棵二叉搜索树，请找出其中第k大的节点。
#示例 1:
#输入: root = [3,1,4,null,2], k = 1
#   3
#  / \
# 1   4
#  \
#   2
#输出: 4
#示例 2:
#输入: root = [5,3,6,2,4,null,null,1], k = 3
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
#输出: 4
################################solution 1 ################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        queue = collections.deque()
        queue.append(root)
        arr = []
        while queue:
            res = queue.pop()
            arr.append(res.val)
            if res.left:
                queue.append(res.left)
            if res.right:
                queue.append(res.right)

        def QuickSort(left, right):
            if left >= right:
                return
            i, j = left, right
            while i < j:
                while i < j and arr[j] <= arr[left]:
                    j -= 1
                while i < j and arr[i] >= arr[left]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[i], arr[left] = arr[left], arr[i]
            QuickSort(left, i - 1)
            QuickSort(i + 1, right)
            return arr
        sort_arr = QuickSort(0, len(arr) - 1)
        return sort_arr[k-1]
################################solution 2 ################################
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root:
                return 
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)
        self.k = k
        dfs(root)
        return self.res

