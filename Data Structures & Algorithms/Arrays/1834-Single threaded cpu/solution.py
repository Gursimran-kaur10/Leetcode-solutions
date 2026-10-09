class Solution(object):
    def getOrder(self, tasks):
        tasks=sorted((e,p,i) for i,(e,p) in enumerate(tasks))

        time=tasks[0][0]
        i=0
        heap=[] #available tasks
        ans=[]

        while heap or i<len(tasks):

            while i<len(tasks) and tasks[i][0]<=time:
                heapq.heappush(heap,(tasks[i][1],tasks[i][2]))
                i+=1
            if not heap:
                time=tasks[i][0]
                continue

            processing,index=heapq.heappop(heap)
            ans.append(index)
            time+=processing
        return ans
        
