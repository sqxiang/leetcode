class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans = []
        candidates.sort()
        use = [0]*len(candidates)
        self.dfs(candidates,0,0,target,[],use)
        return self.ans

    def dfs(self,candidates,p,now,target,tmp,use):
        if now == target:
            self.ans.append(tmp[:])
            return
        for i in range(p,len(candidates)):
            if now+candidates[i] <=target and (i==0 or candidates[i]!=candidates[i-1] or use[i-1]==1):
                tmp.append(candidates[i])
                print 'tmp',tmp
                use[i] = 1
                self.dfs(candidates,i+1,now+candidates[i],target,tmp,use)
                tmp.pop()
                use[i] = 0

solution = Solution()
print solution.combinationSum2([10,1,2,7,6,1,5],8)