from solution import ListNode, Solution


# Create linked list, 1st example
l1_node_0 = ListNode(val=3)
l1_node_1 = ListNode(val=4, next=l1_node_0)
l1_node_2 = ListNode(val=2, next=l1_node_1)

l2_node_0 = ListNode(val=4)
l2_node_1 = ListNode(val=6, next=l2_node_0)
l2_node_2 = ListNode(val=5, next=l2_node_1)

# Create solution
s = Solution()
print(s.addTwoNumbers(l1_node_2, l2_node_2))

# Create linked list, 2nd example
l3_node_0 = ListNode(val=0)

l4_node_0 = ListNode(val=0)

print(s.addTwoNumbers(l3_node_0, l4_node_0))

# Create linked list, 3rd example
l5_node_0 = ListNode(val=9)
l5_node_1 = ListNode(val=9, next=l5_node_0)
l5_node_2 = ListNode(val=9, next=l5_node_1)
l5_node_3 = ListNode(val=9, next=l5_node_2)
l5_node_4 = ListNode(val=9, next=l5_node_3)
l5_node_5 = ListNode(val=9, next=l5_node_4)
l5_node_6 = ListNode(val=9, next=l5_node_5)

l6_node_0 = ListNode(val=9)
l6_node_1 = ListNode(val=9, next=l6_node_0)
l6_node_2 = ListNode(val=9, next=l6_node_1)
l6_node_3 = ListNode(val=9, next=l6_node_2)

print(s.addTwoNumbers(l5_node_6, l6_node_3))
