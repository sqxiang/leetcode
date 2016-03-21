class Solution(object):
    data = {'0':('',),'1':('',),'2':('a','b','c'),
                '3':('d','e','f'),'4':('g','h','i'),'5':('j','k','l'),
                '6':('m','n','o'),'7':('p','q','r','s'),'8':('t','u','v'),
                '9':('w','x','y','z')}
    P,Q,res = list(),list(),list()
    def dfs(self,digits,level):

        if(level==len(digits)):
            self.Q = ''.join(self.P)
            self.res.append(self.Q)
            return self.res
        S = self.data[str(digits[level])]

        for s in S:
            self.P.append(s)
            self.dfs(digits,level+1)
            self.P.pop()

    def letterCombinations(self, digits):
        result = self.dfs(digits,0)
        if("" == digits):
            return []

        return self.res



solution = Solution()
print solution.letterCombinations("2")