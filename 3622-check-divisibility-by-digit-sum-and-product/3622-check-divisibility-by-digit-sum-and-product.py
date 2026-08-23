class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sums=0
        pro=1
        num=n
        while num!=0:
            s=num%10
            sums+=s
            pro*=s
            num//=10
        if n % (sums + pro) == 0:
            return True
        else:
            return False


        