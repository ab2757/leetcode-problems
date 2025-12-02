class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}
        for i in range(len(nums)):
            if(target-nums[i] in hash_dict.keys()):
                return [hash_dict[target-nums[i]],i]
            else:
                hash_dict[nums[i]] = i
        
