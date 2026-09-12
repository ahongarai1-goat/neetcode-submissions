class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        saw={}
        for i in range(n):
            a=nums[i]
            diff=target-nums[i]
            if diff in saw:
                return [saw[diff],i]
            else:
                saw[a]=i

        