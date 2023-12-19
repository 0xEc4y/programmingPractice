class Solution(object):
    def majorityElement(self, nums):
        sortedNums = sorted(nums)

        # Since it's given that a specific number will always be the majority of the list,
        # if sorted, the middle number will always be the majority.
        middle = (len(nums)) // 2

        return sortedNums[middle]