"""
You are given the head of a linked list and the number k, You have to return the kth node from the end of linkedList. If k is more than the number of nodes, then the return -1.

Examples

Input: LinkedList: 1->2->3->4->5->6->7->8->9, k = 2
Output: 8
Explanation: The given linked list is 1->2->3->4->5->6->7->8->9. The 2nd node from end is 8.

Input: LinkedList: 10->5->100->5, k = 5
Output: -1
Explanation: The given linked list is 10->5->100->5. Since 'k' is more than the number of nodes, the output is -1.

Constraints:
1 ≤ number of nodes ≤ 106
1 ≤ node->data , x ≤ 106
1 ≤ k ≤ 106
"""

class Solution:
    def getKthFromLast(self, head, k):
        #code here
        def getLength(head):
            count = 0
            while head is not None:
                head = head.next
                count +=1
            return count
            
        length = getLength(head)
        
        if length <k:
            return -1
        
        curr = head
        for _ in range(length - k):
            curr = curr.next
        return curr.data
    


# Test cases
class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

# Example 1
head1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
k1 = 2
solution = Solution()
print(solution.getKthFromLast(head1, k1))  # Output: 8  