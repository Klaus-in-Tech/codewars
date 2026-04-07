class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt
class Solution:
    def partition(self, head, x):
        #code here
        lessHead = Node(0)
        equalHead = Node(0)
        greaterHead = Node(0)
        
        less = lessHead
        equal = equalHead
        greater = greaterHead
        
        curr = head
        
        while curr:
            if curr.data < x:
                less.next = curr
                less = less.next
            elif curr.data == x:
                equal.next = curr
                equal = equal.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next
            
        greater.next = None
        
        equal.next = greaterHead.next
        
        less.next = equalHead.next
        
        newHead = lessHead.next
        
        return newHead
    
def print_linked_list(head):
    values = []
    current = head
    while current is not None:
        values.append(str(current.data))
        current = current.next
    print(" -> ".join(values) if values else "Empty")   

# Test cases
# Example 1
head1 = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
solution = Solution()
new_head1 = solution.partition(head1, 3)  # Partitions around value 3
print_linked_list(new_head1)  # Output: 1 -> 2 -> 2 -> 3 -> 4 -> 5