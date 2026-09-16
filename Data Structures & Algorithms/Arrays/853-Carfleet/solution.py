class Solution(object):
    def carFleet(self, target, position, speed):
        stack=[]
        cars=sorted(zip(position,speed),reverse=True)

        for pos,spd in cars:
            time=float(target-pos)/spd
            if not stack or time>stack[-1]:
                stack.append(time)
        retrun len(stack)
        
