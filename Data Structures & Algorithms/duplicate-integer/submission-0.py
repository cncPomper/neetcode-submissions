class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = []
        for element in nums:
            if element not in visited:
                visited.append(element)
            else:
                return True
        return False