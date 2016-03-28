class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==1):
            return 1
        j = 0
        while(j<len(nums)-1):
            if(nums[j+1]==nums[j]):
                nums.pop(j)
            else:
                j+=1
        return len(nums)
solution = Solution()
print solution.removeDuplicates([1,1,2,2,2,2,3])