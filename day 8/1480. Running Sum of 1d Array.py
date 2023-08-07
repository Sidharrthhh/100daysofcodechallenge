class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            runningSum = 0
            for j in range(i+1):
                runningSum += nums[j]
            ans.append(runningSum)
        return ans 