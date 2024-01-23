class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # create stack
        stack = []
        
        for i in range(len(s)):
            # if we encounter open bracket, then add it to stack
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                # if stack is empty, something was wrong, parentheses not in correct order for sure
                if len(stack) == 0:
                    return False
                
                # pop last bracket from stack
                last = stack.pop()
                
                # check if brackets are in correct order
                # if they are, then proceed with checking
                # if not return false
                if (s[i] == ')' and last == '(') or (s[i] == ']' and last == '[') or (s[i] == '}' and last == '{'):
                    pass
                else:
                    return False
        
        # if stack is not empty, something is wrong, return false
        if len(stack) > 0:
            return False
         
        # return true
        return True
