class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # create two pointers and result variable
        left = 0
        right = len(height) - 1
        res = 0
        
        # loop until left pointer is less than right pointer
        while left < right:
            # get minimum height between two pointed by pointers 
            m = min(height[left], height[right])
            
            # calculate area
            r = m * (right - left)
            
            # if calculated area os bigger than previous, save it
            if r > res:
                res = r
            
            # if lower height is on the left, then increment left pointer
            # otherwise increment right pointer
            if m == height[left]:
                left = left + 1
            else:
                right = right - 1
            
        # return result
        return res
