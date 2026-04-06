class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt


def print_linked_list(head):
    values = []
    current = head
    while current is not None:
        values.append(str(current.data))
        current = current.next
    print(" -> ".join(values) if values else "Empty")

class Solution:
    def deleteNode(self, head):
        # Delete the middle node of the linked list
        if head is None or head.next is None:
            return None

        prev = None
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head
    

# Test cases
# Example 1
head1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
solution = Solution()
new_head1 = solution.deleteNode(head1)  # Deletes the middle node (3)
print_linked_list(new_head1)  # Output: 1 -> 2 -> 4 -> 5