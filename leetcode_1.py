class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # dict

        for i,n in enumerate(nums): # 1, 7
            diff = target - n # 2
            if diff in prevMap: # 2 in prevMap = {}
                return [prevMap[diff], i] # {0,1}
            prevMap[n] = i # prevMap = {0}
