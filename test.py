class Solution(object):
    def longestPalindrome(self, s):
        res = ''
        for i in range(len(s)):
            l,r = i,i
            el,er = i,i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            while(el>=0 and er<len(s) and s[el]==s[er]):
                el-=1
                er+=1
            if(r-l>er-el):
                tmp = s[l+1:r]
            else:
                tmp = s[el+1:er]
            if(len(tmp)>len(res)):
                res = tmp
        return res

solution = Solution()
print solution.longestPalindrome('aacbcaacaacb')