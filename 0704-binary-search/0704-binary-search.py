class Solution(object):
    def search(self, nums, n):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        u=len(nums)-1
        while l<=u:
            mid=(l+u)//2
            if nums[mid]==n:
                # globals()['pos']=mid
                return mid
            else:
                if nums[mid]<n:
                    l=mid+1
                else:
                    u=mid-1
        return -1
            