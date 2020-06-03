class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        a = sorted(costs, key=lambda x: x[0]-x[1])
        Sa = 0
        Sb = 0
        for i in range(len(a)//2):
            Sa += a[i][0]
            
        for i in range(len(a)//2, len(a)):
            Sb += a[i][1]
        return Sa + Sb