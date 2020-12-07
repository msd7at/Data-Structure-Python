class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        l=[1]*(n+1)
        m=1
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j] and l[j]>=l[i]:
                    l[i]=l[j]+1
                    m=max(m,l[i])
        # print(l)
        return m        
            