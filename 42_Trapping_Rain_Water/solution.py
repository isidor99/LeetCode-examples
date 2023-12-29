class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Create variables
        res = 0
        stack = []
        
        for i, num in enumerate(height):
            while len(stack) != 0 and height[stack[-1]] < num:
                # Get value at the top of stack
                top = stack.pop()
                
                # If stack is empty, break the loop
                if len(stack) == 0:
                    break
                
                # Calculate distance
                distance = i - stack[-1] - 1
                
                # Calculate minimal height
                min_height = min(height[stack[-1]], num) - height[top]
                
                # Add to result
                res = res + distance * min_height
                
            # Append element to stack
            stack.append(i)
    
        # Return result
        return res
                