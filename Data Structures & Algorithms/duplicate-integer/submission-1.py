class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Sorting the values
        seen = set()
        
    # Iterate through each element
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False