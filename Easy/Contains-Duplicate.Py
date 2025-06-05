# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Example 1:
    # Input: nums = [1, 2, 3, 3]
    # Output: true

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         return len(set(nums)) < len(nums) # len(nums) = total number of elements (including duplicates) and len(set(nums)) = number of unique elements

# If duplicates exist, then it the total number of unique elements has to be smaller than total number of elements (True)
# If theres no dupicates then # of unique elements will match the total # of elements (False)