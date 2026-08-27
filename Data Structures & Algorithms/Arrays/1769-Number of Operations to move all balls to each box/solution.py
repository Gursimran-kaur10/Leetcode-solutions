class Solution(object):
    def minOperations(self, boxes):
        n=len(boxes)
        result=[0]*n
        balls=0
        moves=0
        for i in range(n):
            result[i]+=moves # not looking at current position ball 
            if boxes[i]=='1':
                balls+=1

            moves+=balls
        
        balls=0
        moves=0

        for i in range(n-1,-1,-1):
            result[i]+=moves
            if boxes[i]=='1':
                balls+=1
            
            moves+=balls
        return result

        
