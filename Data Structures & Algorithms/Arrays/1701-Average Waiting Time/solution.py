class Solution(object):
    def averageWaitingTime(self, customers):
        wait_time=[]
        current_time=0
        for arrival,prep in customers:
            current_time=max(arrival,current_time)
            current_time+=prep
            waiting=current_time-arrival
            wait_time.append(waiting)
        return float(sum(wait_time))/len(wait_time)
        
