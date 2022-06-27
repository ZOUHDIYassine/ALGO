# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:55:44 2022

@author: toshiba
"""

class Solution(object):  
    def minimumSum(self,num):
        srt_num = sorted([int(i) for i in list(str(num))])
        new_1 = str(srt_num[0]) + str(srt_num[2])
        new_2 = str(srt_num[1]) + str(srt_num[3])
        return int(new_1) + int(new_2)