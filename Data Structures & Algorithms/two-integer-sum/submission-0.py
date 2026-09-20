class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapSet = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in mapSet:
                return [mapSet[diff], idx]
            mapSet[num] = idx

        return []