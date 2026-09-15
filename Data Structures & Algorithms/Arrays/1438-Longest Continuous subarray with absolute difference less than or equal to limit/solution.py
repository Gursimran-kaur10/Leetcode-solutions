class Solution(object):
    def longestSubarray(self, nums, limit):
        maxdeque=deque() #store indices only not number
        mindeque=deque()
        left=0
        ans=0

        for right in range(len(nums)):

            while maxdeque and nums[maxdeque[-1]]<nums[right]:
                maxdeque.pop()
            while mindeque and nums[mindeque[-1]]>nums[right]:
                mindeque.pop()
            maxdeque.append(right)
            mindeque.append(right)

            while nums[maxdeque[0]]-nums[mindeque[0]]>limit:

                if maxdeque[0]==left:
                    maxdeque.popleft()#to pop from start 
                if mindeque[0]==left:
                    mindeque.popleft()
                left+=1
            ans=max(ans,right-left+1)
        return ans

        
