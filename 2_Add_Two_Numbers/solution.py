class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def __str__(self):
        res_list = []
        tmp = self
        
        # Loop through and add value to array
        while tmp != None:
            res_list.append(tmp.val)
            
            # Update temp variable
            tmp = tmp.next

        # Return string representation of array
        return str(res_list)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # Create list head and temporary pointers
        head = tmp = None       
        p = 0
        
        while l1 != None or l2 != None:
            # Calculate sum
            sum = (l1.val if l1 != None else 0) + (l2.val if l2 != None else 0) + p
            v = sum % 10
            p = sum // 10

            # Create new node
            new_node = ListNode(val=v)
            
            if head == None:
                head = tmp = new_node
            else:
                tmp.next = new_node
                tmp = new_node
            
            # Update list pointers
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        
        # If p is not 0, then add new node
        if p > 0:
            tmp.next = ListNode(val=p)
        
        # Return result
        return head
