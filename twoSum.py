class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results = list()
        if (len(nums)==1):
            return []
        for i in range(0,len(nums)):
            if((target-nums[i]) in nums[i+1:]):
                #print target-nums[i],nums[i+1:]
                results.append(i)
                results.append(nums[i+1:].index(target-nums[i])+i+1)
                return results

solution = Solution()
print solution.twoSum([0,4,3,0],0)

