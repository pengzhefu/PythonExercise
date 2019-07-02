# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:21:33 2019

@author: pengz
"""

'''
微软中国三面的内容
'''
def getMissing(nums):  ## time is O(logN)
    start = 0
    end = len(nums) -1
    while start < end:
        mid = (start+end) //2  ## cal the middle
        if nums[mid] != mid+1:
            end = mid
        else:
            start = mid+1
#        if (nums[start]-start) != (nums[mid] -mid):   ## it should be 1, if not, it should be 2
#            ## if not equal, move end
#            end = mid
#        elif (nums[end] - end) != (nums[mid] -mid):
            ## move start
#            start = mid+1
    if start == 0:
        return 1
    elif start == len(nums)-1:
        return 0
    else:
        return nums[start]-1


print(getMissing([1,2,3,4,5]))