# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #a -> b! -> c -> d
        #a <- b! -> c -> d
        if not head:
            return head
        next_node=head.next
        previous=None
        while head:
            next_node=head.next #b
            head.next= previous# b -> a
            previous=head
            head=next_node #b

        return previous
