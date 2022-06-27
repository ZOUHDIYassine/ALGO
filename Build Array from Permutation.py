# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:48:31 2022

@author: toshiba
"""

class Solution(object):
    def buildArray(self, nums):
        l=[]
        for i in range(len(nums)):
            l.append(nums[nums[i]])
        return(l)
        