#请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
#示例1：
#输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
#输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
#示例2：
#输入：head = [[1,1],[2,1]]
#输出：[[1,1],[2,1]]
#示例3：
#输入：head = [[3,null],[3,0],[3,null]]
#输出：[[3,null],[3,0],[3,null]]
#示例4：
#输入：head = []
#输出：[]
#解释：给定的链表为空（空指针），因此返回 null。
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
           return
        cur = head
        dic = {}
        while cur:
            dic[cur] = Node(cur.val)
            cur=cur.next
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]


