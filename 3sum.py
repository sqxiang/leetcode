class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums)<3):
            return []
        s = list()
        nums.sort()
        for i in range(0,len(nums)-2):
            j = i+1
            k = len(nums)-1
            while(j<k):
                ans = nums[i]+nums[j]+nums[k]
                if(ans==0):
                    if( [nums[i],nums[j],nums[k]] not in s):
                        s.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                if(ans<0):
                    j+=1
                if(ans>0):
                    k-=1

        return s

solution = Solution()
print solution.threeSum([-1,0,1,2,-1,3])

