class Solution(object):
    def getRow(self, rowIndex):
        row=[1]
        current =1
        for i in range(rowIndex):
            current=current*(rowIndex-i)//(i+1)
            row.append(current)
        return row
        
