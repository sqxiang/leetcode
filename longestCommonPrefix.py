class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs)<=1):
            return strs[0] if len(strs)==1 else ""
        end,minl= 0,min([len(strs[i]) for i in range(len(strs))])
        while(end<minl):
            for i in range(1,len(strs)):
                if(strs[i][end]!=strs[i-1][end]):
                    return strs[0][:end]
            end+=1
        return strs[0][:end]




