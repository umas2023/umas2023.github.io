from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:  # 递归边界：l1 和 l2 都是空节点
            return ListNode(carry) if carry else None  # 如果进位了，就额外创建一个节点
        if l1 is None:  # 如果 l1 是空的，那么此时 l2 一定不是空节点
            l1, l2 = l2, l1  # 交换 l1 与 l2，保证 l1 非空，从而简化代码
        carry += l1.val + (l2.val if l2 else 0)  # 节点值和进位加在一起
        l1.val = carry % 10  # 每个节点保存一个数位
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, carry // 10)  # 进位
        return l1


l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))

ans = Solution().addTwoNumbers(l1=l1, l2=l2)
print(ans.val)
print(ans.next.val)
print(ans.next.next.val)
