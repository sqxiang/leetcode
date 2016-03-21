import sys
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        minint = -sys.maxint
        maxint = sys.maxint
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        n1,n2= len(nums1),len(nums2)
        if n1 == 0:
            return (nums2[(n2-1)/2]+nums2[n2/2])/2.0
        imin,imax= 0,2*n1
        while(imin<=imax):
            c1 = (imin+imax)/2
            #print 'c1 ',c1
            c2 = n1 + n2 -c1
            #print 'c2 ',c2
            if c1 == 0:
                l1 = minint
            else:
                l1 = nums1[(c1-1)/2]
                #print 'l1 ',l1
            if c1 == 2*n1:
                r1 = maxint
            else:
                r1 = nums1[(c1)/2]
                #print 'r1 ',r1
            if (c2 == 0):
                l2 = minint
            else:
                l2 = nums2[(c2-1)/2]
                #print 'l2 ',l2
            if(c2 == 2*n2):
                r2 = maxint
            else:
                r2 = nums2[c2/2]
                #print 'r2 ',r2
            if(l1>r2):
                imax = c1 - 1
                #print 'imax ',imax
            elif(l2>r1):
                imin = c1 + 1
                #print 'imin ',imin
            else:
                return (max(l1,l2)+min(r1,r2))/2.0


solution = Solution()
print solution.findMedianSortedArrays([0,1,7],[1,2,3,3,4,5])