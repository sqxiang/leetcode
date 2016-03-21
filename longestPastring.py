
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        flag = dict()
        maxlen = 1
        start = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if i>=j:
                    flag[i,j] = True
                else:
                    flag[i,j] = False
        for j in range(1,len(s)):
            for i in range(0,j):
                if(s[i] == s[j]):
                    flag[i,j] = flag[i+1,j-1]
                    if(flag[i,j] and j-i+1>maxlen):
                        maxlen = j-i+1
                        start = i
        return s[start:start + maxlen]




solution = Solution()
print solution.longestPalindrome('aabbaac')

