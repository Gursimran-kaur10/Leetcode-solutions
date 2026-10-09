class Solution(object):
    def leastInterval(self, tasks, n):
        freq={}
        

        for task in tasks:
            freq[task]=freq.get(task,0)+1
        fmax=max(freq.values())

        # Count tasks having maximum frequency
        count_max = 0
        for f in freq.values():
            if f == fmax:
                count_max += 1

        # Apply formula
        intervals = (fmax - 1) * (n + 1) + count_max

        # Return the minimum required intervals
        return max(len(tasks), intervals)


'''famx represent number of gap or group like a=3 then a_ _ a _ _ a        2 groups 
n+1 each group length 
multiply fmax and n+1 for total length before final occurence
+cmax last occurence '''
