class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        if height==[]:
            return 0
        h1 = max(height)
        l1 = height.index(h1)
        r1 = len(height)-height[::-1].index(h1)-1
        lindex = l1
        rindex = r1
        for i in range(lindex+1,rindex):
            ans+=(h1-height[i])
        while(lindex>0):
            h1 = max(height[0:lindex])
            rindex = lindex
            lindex = lindex-1-height[0:lindex][::-1].index(h1)
            for i in range(lindex+1,rindex):
                ans+=(h1-height[i])
        lindex = l1
        rindex = r1
        while(rindex<len(height)-1):
            h1 = max(height[rindex+1:])
            lindex = rindex
            rindex = height[rindex+1:].index(h1)+rindex+1
            for i in range(lindex+1,rindex):
                ans+=(h1-height[i])
        return ans

solution = Solution()
print solution.trap([2,0,2])
