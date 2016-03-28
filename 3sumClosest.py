class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = None
        for i in range(len(nums)):
            l,r = i+1,len(nums)-1
            while(l<r):
                sum = nums[i]+nums[l]+nums[r]
                if ans is None or abs(target-sum)<abs(target-ans):
                    ans = sum
                if sum<=target:
                    l+=1
                else:
                    r-=1
        return ans
