class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # output = [1] * n

        # prefix = 1
        # for i in range(n):
        #     output[i] = prefix
        #     prefix *= nums[i]

        # suffix = 1
        # for i in range(n-1, -1, -1):
        #     output[i] *= suffix
        #     suffix *= nums[i]

        # return output
        output = [0] * n
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = suffix[n-1] = 1
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]

        for i in range(n):
            output[i] = prefix[i] * suffix[i]

        return output
        