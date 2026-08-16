class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ct=0
        n=len(nums)
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                ct+=1
        if nums[-1]>nums[0]:
            ct+=1
        return ct<=1