class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = str(n)
        while(n-1):
            s = self.make(s)
            print s
            n-=1
        return s

    def make(self,s):
        count,ans = 1,''
        if len(s) == 1:
            return '1'+s
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count+=1
            else:
                ans+=str(count)+s[i-1]
                count=1
        ans+=str(count)+s[i]
        return ans

solution = Solution()
print solution.countAndSay(12)