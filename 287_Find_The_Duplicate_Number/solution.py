class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # linked list problem
        # Floyd's cycle finding algorithm
        slow = fast = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break

        finder = 0
        
        while True:
            slow = nums[slow]
            finder = nums[finder]
            
            if slow == finder:
                return slow
