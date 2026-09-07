class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        satisfied=0

        for i in range(len(customers)):
            if grumpy[i]==0:
                satisfied+=customers[i]
        extra=0
        for i in range(minutes):
            if grumpy[i]==1:
                extra+=customers[i]
        max_extra=extra

        for i in range(minutes,len(customers)):
            if grumpy[i-minutes]==1:
                extra-=customers[i-minutes]
            if grumpy[i]==1:
                extra+=customers[i]
            max_extra=max(extra,max_extra)
        return satisfied+max_extra

        
