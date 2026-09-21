class Solution(object):
    def shipWithinDays(self, weights, days):
        left=max(weights)
        right=sum(weights)

        while left<=right:
            capacity=(left+right)//2
            current_weight=0
            req_day=1
            for weight in weights:
                if current_weight+weight>capacity:
                    req_day+=1
                    current_weight=weight
                else:
                    current_weight+=weight
            if req_day<=days:
                right=capacity-1
            else:
                left=capacity+1
        return left

        
