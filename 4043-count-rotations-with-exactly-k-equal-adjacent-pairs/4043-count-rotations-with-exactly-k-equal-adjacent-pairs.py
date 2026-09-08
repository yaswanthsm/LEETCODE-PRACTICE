class Solution(object):
    def countRotations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n=len(s)
        ct=0
        for i in range(n):
            if s[i]==s[(i+1)%n]:
                ct+=1
        ans = 0
        for i in range(n):
            score = ct

            if s[i] == s[(i + 1) % n]:
                score -= 1

            if score == k:
                ans += 1

        return ans