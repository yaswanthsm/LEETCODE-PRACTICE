class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        power=1000
        commas=1
        while power<=n:
            ans+=n-power+1
            power*=1000
            commas+=1
        return ans
        