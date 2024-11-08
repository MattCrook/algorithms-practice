#------------------------------------------------#
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#------------------------------------------------#



#---------- LINKED LIST LONGE APPROACH: ---------------#
# Initialization: We will traverse both linked lists, adding the corresponding digits from each list, along with any carry from the previous step.
# Carry: If the sum of the two digits is greater than or equal to 10, we carry over the excess to the next digit.
# Linked List Creation: For each sum, we will create a new node to represent the result and continue until both lists are exhausted.
# End of Lists: If one list is shorter, treat the missing digits as 0. At the end of the lists, if there's still a carry, add a new node for the carry.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution_3:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize a dummy head to simplify the code
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        # Traverse through both linked lists
        while l1 or l2 or carry:
            # Get the values of the current nodes, or 0 if the node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Compute the sum of the two digits and the carry
            total = val1 + val2 + carry

            # The new digit is total % 10 (i.e., the ones place)
            carry = total // 10  # The carry for the next iteration
            current.next = ListNode(total % 10)

            # Move the current pointer to the next node
            current = current.next

            # Move the pointers to the next nodes in the input lists, if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # The result is in the next node of the dummy head
        return dummy_head.next

#-------- Helper function to create a linked list from a list of digits ------------#
def create_linked_list(nums):
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# Create linked lists for the example
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

# Solve the problem
solution_3 = Solution_3()
result = solution_3.addTwoNumbers(l1, l2)
print("SOLUTION_03:")
print_linked_list(result)  # Output: 7 -> 0 -> 8
