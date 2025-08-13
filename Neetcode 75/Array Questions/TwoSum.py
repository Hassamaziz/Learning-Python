# Two Sum 
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevNum = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in prevNum:
                return [prevNum[diff],i]
            prevNum[n]=i
        return