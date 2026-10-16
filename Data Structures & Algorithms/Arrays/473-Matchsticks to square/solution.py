class Solution(object):
    def makesquare(self, matchsticks):
        total=sum(matchsticks)

        if total %4!=0:
            return False
        target=total//4
        matchsticks.sort(reverse=True)
        sides=[0]*4

        def dfs(index):
            if index==len(matchsticks):
                return True
            stick=matchsticks[index]

            for i in range(4):
                if sides[i]+stick<=target:
                    sides[i]+=stick

                    if dfs(index+1):
                        return True
                    sides[i]-=stick
                if sides[i]==0:
                    break
            return False
        return dfs(0)

            
        
