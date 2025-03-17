from collections import deque

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        if n==1:
            return 1

        trust_count={}
        trust_by_count={}


        for element in trust:
            trust_count[element[0]] = trust_count.get(element[0],0) + 1
            trust_by_count[element[1]] = trust_by_count.get(element[1],0) + 1
            

        for person in range(1,n+1):
            if trust_count.get(person,0) == 0 and trust_by_count.get(person,0) == n-1:
                return person

        return -1