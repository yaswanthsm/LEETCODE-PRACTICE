class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        a=0
        while n!=0:
            d=n%10
            n//=10
            if d>a:
                s=a
                a=d
            elif d>s:
                s=d

        return a*s

            


        