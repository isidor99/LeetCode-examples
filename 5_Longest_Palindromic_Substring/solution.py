class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # define the subproblem
        # initialize the base case
        dp = [[True if i == j else False for i in range(len(s))] for j in range(len(s))]
        
        # track longest palindromic substring
        start, max_len = 0, 1
        
        # check substrings of length 2
        for i in range(len(s) - 1):
            
            # check if two characters are the same
            if s[i + 1] == s[i]:
                
                # save result to matrix
                dp[i][i + 1] = True
                
                # save start index and max length
                start = i
                max_len = 2

        # check substrings of length 2
        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                
                # calculate j from i
                j = i + length - 1
                
                # check if equals
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    
                    # save result to matrix
                    dp[i][j] = True
                    
                    # save start index and max length
                    start = i
                    max_len = length
                
        # return result
        return s[start:start + max_len]
