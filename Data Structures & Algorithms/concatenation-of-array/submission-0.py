class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        # ans[0 + 9 = 9] == nums[0]
        # ans[1 + 9 = 10] == nums[1]
        # ...
        # ans[8 + 9 = 17] == nums[17]

        return ans