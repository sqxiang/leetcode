class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)==0 and len(haystack)!= 0:
            return -1
        if len(needle)==0 and len(haystack)==0:
            return 0
        next = self.makeNext(needle)
        print next
        k = 0
        for i in range(0,len(haystack)):
            while(k>0 and haystack[i]!=needle[k]):
                k = next[k-1]
            if(haystack[i]==needle[k]):
                k+=1
            if(k == len(needle)):
                return i-k+1
        return -1



    def makeNext(self,needle):
        length = len(needle)
        next = [0]*length
        next[0] = 0
        k,q = 0,1
        while(q<length):
            while(k>0 and needle[q]!=needle[k]):
                k = next[k-1]
            if needle[q] == needle[k]:
                k+=1
            next[q] = k
            q+=1
        return next

solution = Solution()
print solution.strStr('abcaabcsabsabcsabcw','abcsabc')