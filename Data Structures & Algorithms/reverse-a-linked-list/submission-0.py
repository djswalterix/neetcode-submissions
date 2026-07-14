# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None          # what's behind the first node?
        current = head
        while current:
            next_node = current.next     # save the path forward BEFORE you destroy it
            current.next = previous  # flip the arrow backward
            previous = current      # everyone shifts: "behind me" becomes current
            current = next_node       # advance to the node I saved
        return previous              # at the end, which pointer is the new head?