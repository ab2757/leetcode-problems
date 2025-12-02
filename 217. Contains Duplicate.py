class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in range(len(nums)):
            if(nums[i] in dict.keys()):
                return True
            else:
                dict[nums[i]] = i
        return False

        
