class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        self.dfs(0,0,n,'',self.ans)
        return self.ans

    def dfs(self,l,r,n,str,p):
        if(r==n and l==r):
            p.append(str)
            return p
        if(l<n):
            self.dfs(l+1,r,n,str+'(',p)
        if(r<l):
            self.dfs(l,r+1,n,str+')',p)

solution = Solution()
print solution.generateParenthesis(3)