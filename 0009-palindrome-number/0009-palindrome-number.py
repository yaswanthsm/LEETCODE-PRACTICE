class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        st=str(x)
        num=list(st)
        num=list(reversed(num))
        if list(st)==num:
            return True
        return False
        
