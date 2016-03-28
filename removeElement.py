class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.sort()
        if(val not in nums):
            return len(nums)
        j = nums.index(val)
        while(j<len(nums) and nums[j]==val):
            nums.pop(j)
        return len(nums)

solution = Solution()
print solution.removeElement([3,2,2,3],3)