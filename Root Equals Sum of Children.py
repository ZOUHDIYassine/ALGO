# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:49:48 2022

@author: toshiba
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def checkTree(self, root):
        return (root.val == (root.left.val + root.right.val))