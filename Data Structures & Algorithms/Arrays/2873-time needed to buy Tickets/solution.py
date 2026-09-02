class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        time=0
        i=0

        while True:
            if tickets[i]>0:
                tickets[i]-=1
                time+=1
            if i==k and tickets[i]==0:
                return time
            i+=1
            if i==len(tickets):
                i=0

        return time

'''
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        time=0
        for i in range(len(tickets)):
            if i<=k:
                time+=min(tickets[i],tickets[-1])
            else:
                time+=min(tickets[i],tickets[k]-1)
        return time
'''
