
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    

class SolveReverseLinkedList:
    def reverse_list(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
    

n1 = ListNode()
n1.val = 1
n2 = ListNode()
n2.val = 2
n3 = ListNode()
n3.val = 3
n4 = ListNode()
n4.val = 4
n5 = ListNode()
n5.val = 5


