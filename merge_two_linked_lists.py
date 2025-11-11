class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        prehead = ListNode()
        tail = prehead

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return prehead.next

                
def build_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)


if __name__ == "__main__":
    l1 = build_linked_list([1, 3, 5, 7])
    l2 = build_linked_list([2, 4, 6, 8, 10])
    sol = Solution()
    merged_head = sol.mergeTwoLists(l1, l2)
    print_linked_list(merged_head)