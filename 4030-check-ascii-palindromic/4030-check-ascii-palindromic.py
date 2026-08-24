class Solution(object):
    def isPalindromic(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=""
        for i in s:
            asc=ord(i)
            bi=bin(asc)[2:].zfill(8)
            st+=bi
        return st==st[::-1]

