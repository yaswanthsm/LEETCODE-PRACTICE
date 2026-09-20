class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # lst=[]
        n=len(numbers)
        # for i in range(n):
        #     for j in range (i+1,n):
        #         if numbers[i]+numbers[j]==target:
        #             # lst.append(i+1,j+1)
        #             return[i+1,j+1]
        l=0
        r=len(numbers)-1
        while l<r:
            tot=numbers[l]+numbers[r]
            if tot==target:
                return [l+1,r+1]
            elif target>tot:
                l+=1
            else:
                r-=1