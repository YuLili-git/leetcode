#输入两个链表，找出它们的第一个公共节点。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            if A:
                A = A.next
            else:
                A = headB
            if B:
                B = B.next
            else:
                B = headA
        return A
